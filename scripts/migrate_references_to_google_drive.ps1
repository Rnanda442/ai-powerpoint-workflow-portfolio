[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$DriveRoot,
    [string]$NorthSlopeRepo,
    [string]$LibraryName = "Codex Project Reference Library",
    [int]$MaxFileSizeMB = 750,
    [switch]$IncludeLargeFiles
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot

function Find-GoogleDriveRoot {
    $candidates = @(
        "G:\My Drive",
        "H:\My Drive",
        (Join-Path $env:USERPROFILE "My Drive"),
        (Join-Path $env:USERPROFILE "Google Drive\My Drive")
    )

    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate -PathType Container) {
            return (Resolve-Path -LiteralPath $candidate).Path
        }
    }

    throw "Google Drive Desktop was not found. Start Google Drive Desktop, then rerun with -DriveRoot 'G:\My Drive' (or your actual My Drive path)."
}

function Test-BlockedPath {
    param([Parameter(Mandatory)][string]$Path)

    $normalized = $Path.Replace("/", "\").ToLowerInvariant()
    $blockedSegments = @(
        "\.git\",
        "\.ssh\",
        "\appdata\",
        "\data_runtime\",
        "\outputs_runtime\",
        "\models_runtime\",
        "\logs_runtime\",
        "\configs_local\",
        "\.auth-cache\",
        "\.dashboard-sync\",
        "\node_modules\",
        "\.venv\",
        "\venv\"
    )
    $blockedNames = @(
        ".env",
        "secrets.toml",
        "credentials.json",
        "token.json",
        "robinhood_token.txt",
        "robinhood_token-copy1.txt"
    )

    foreach ($segment in $blockedSegments) {
        if ($normalized.Contains($segment)) {
            return $true
        }
    }

    return $blockedNames -contains ([System.IO.Path]::GetFileName($normalized))
}

function Get-SafeName {
    param([Parameter(Mandatory)][string]$Name)

    $safe = $Name
    foreach ($character in [System.IO.Path]::GetInvalidFileNameChars()) {
        $safe = $safe.Replace($character, "_")
    }
    return $safe.Trim()
}

function Add-Candidate {
    param(
        [System.Collections.Generic.List[object]]$Candidates,
        [string]$SourcePath,
        [Parameter(Mandatory)][string]$Collection,
        [Parameter(Mandatory)][string]$Group,
        [Parameter(Mandatory)][string]$Title,
        [Parameter(Mandatory)][string]$Inventory
    )

    if ([string]::IsNullOrWhiteSpace($SourcePath)) {
        return
    }

    $Candidates.Add([pscustomobject]@{
        SourcePath = $SourcePath.Trim()
        Collection = Get-SafeName $Collection
        Group      = Get-SafeName $Group
        Title      = $Title
        Inventory  = $Inventory
    })
}

function Import-Candidates {
    $items = [System.Collections.Generic.List[object]]::new()

    $sourceInventory = Join-Path $repoRoot "data\source_inventory.csv"
    if (Test-Path -LiteralPath $sourceInventory) {
        foreach ($row in Import-Csv -LiteralPath $sourceInventory) {
            Add-Candidate $items $row.source_path "Portfolio Sources" $row.category $row.title "source_inventory.csv"
        }
    }

    $visualInventory = Join-Path $repoRoot "data\project_visuals.csv"
    if (Test-Path -LiteralPath $visualInventory) {
        foreach ($row in Import-Csv -LiteralPath $visualInventory) {
            Add-Candidate $items $row.source_path "Project Visuals" $row.project_key $row.title "project_visuals.csv"
        }
    }

    $caseStudies = Join-Path $repoRoot "data\case_studies.csv"
    if (Test-Path -LiteralPath $caseStudies) {
        foreach ($row in Import-Csv -LiteralPath $caseStudies) {
            Add-Candidate $items $row.local_path "Case Studies" $row.key $row.title "case_studies.csv"
        }
    }

    $notebooks = Join-Path $repoRoot "data\notebook_inventory.csv"
    if (Test-Path -LiteralPath $notebooks) {
        foreach ($row in Import-Csv -LiteralPath $notebooks) {
            $group = if ($row.tags) { ($row.tags -split ";")[0].Trim() } else { "Uncategorized" }
            Add-Candidate $items $row.path "Notebook Archive" $group $row.title "notebook_inventory.csv"
        }
    }

    if ($NorthSlopeRepo) {
        $manifest = Join-Path $NorthSlopeRepo "docs\source_library_index\source_manifest.csv"
        if (Test-Path -LiteralPath $manifest) {
            foreach ($row in Import-Csv -LiteralPath $manifest) {
                $preferred = if (Test-Path -LiteralPath $row.LibraryPath) { $row.LibraryPath } else { $row.SourcePath }
                Add-Candidate $items $preferred "North Slope Public Source Library" $row.Category $row.File "source_manifest.csv"
            }
        }
    }

    return $items
}

if (-not $DriveRoot) {
    $DriveRoot = Find-GoogleDriveRoot
}
if (-not (Test-Path -LiteralPath $DriveRoot -PathType Container)) {
    throw "Drive root does not exist: $DriveRoot"
}

$destinationRoot = Join-Path $DriveRoot $LibraryName
$reportRoot = Join-Path $destinationRoot "_migration_reports"
[System.IO.Directory]::CreateDirectory($reportRoot) | Out-Null

$candidates = Import-Candidates
$seen = @{}
$report = [System.Collections.Generic.List[object]]::new()
$maxBytes = $MaxFileSizeMB * 1MB

foreach ($candidate in $candidates) {
    $source = $candidate.SourcePath

    if (Test-BlockedPath $source) {
        $report.Add([pscustomobject]@{
            Status = "blocked"
            Source = $source
            Destination = ""
            Bytes = 0
            Inventory = $candidate.Inventory
            Note = "Sensitive or authorized-runtime path"
        })
        continue
    }

    if (-not (Test-Path -LiteralPath $source)) {
        $report.Add([pscustomobject]@{
            Status = "missing"
            Source = $source
            Destination = ""
            Bytes = 0
            Inventory = $candidate.Inventory
            Note = "Not present on this computer"
        })
        continue
    }

    $sourceItems = if (Test-Path -LiteralPath $source -PathType Container) {
        Get-ChildItem -LiteralPath $source -File -Recurse -ErrorAction SilentlyContinue
    } else {
        Get-Item -LiteralPath $source
    }

    foreach ($sourceItem in $sourceItems) {
        if (Test-BlockedPath $sourceItem.FullName) {
            continue
        }

        $key = $sourceItem.FullName.ToLowerInvariant()
        if ($seen.ContainsKey($key)) {
            continue
        }
        $seen[$key] = $true

        if (-not $IncludeLargeFiles -and $sourceItem.Length -gt $maxBytes) {
            $report.Add([pscustomobject]@{
                Status = "large-skipped"
                Source = $sourceItem.FullName
                Destination = ""
                Bytes = $sourceItem.Length
                Inventory = $candidate.Inventory
                Note = "Larger than $MaxFileSizeMB MB; rerun with -IncludeLargeFiles"
            })
            continue
        }

        $targetDirectory = Join-Path $destinationRoot (Join-Path $candidate.Collection $candidate.Group)
        [System.IO.Directory]::CreateDirectory($targetDirectory) | Out-Null
        $target = Join-Path $targetDirectory $sourceItem.Name

        if (Test-Path -LiteralPath $target) {
            $existing = Get-Item -LiteralPath $target
            if ($existing.Length -eq $sourceItem.Length) {
                $report.Add([pscustomobject]@{
                    Status = "already-present"
                    Source = $sourceItem.FullName
                    Destination = $target
                    Bytes = $sourceItem.Length
                    Inventory = $candidate.Inventory
                    Note = "Same filename and size"
                })
                continue
            }

            $suffix = (Get-FileHash -LiteralPath $sourceItem.FullName -Algorithm SHA256).Hash.Substring(0, 10)
            $target = Join-Path $targetDirectory ("{0}_{1}{2}" -f $sourceItem.BaseName, $suffix, $sourceItem.Extension)
        }

        if ($PSCmdlet.ShouldProcess($sourceItem.FullName, "Copy to $target")) {
            Copy-Item -LiteralPath $sourceItem.FullName -Destination $target -Force
            $copied = Get-Item -LiteralPath $target
            if ($copied.Length -ne $sourceItem.Length) {
                throw "Verification failed for $($sourceItem.FullName)"
            }
        }

        $report.Add([pscustomobject]@{
            Status = if ($WhatIfPreference) { "would-copy" } else { "copied" }
            Source = $sourceItem.FullName
            Destination = $target
            Bytes = $sourceItem.Length
            Inventory = $candidate.Inventory
            Note = ""
        })
    }
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$reportPath = Join-Path $reportRoot "reference-migration-$timestamp.csv"
$summaryPath = Join-Path $reportRoot "reference-migration-$timestamp.txt"
$report | Export-Csv -LiteralPath $reportPath -NoTypeInformation -Encoding UTF8 -WhatIf:$false

$summary = $report |
    Group-Object Status |
    Sort-Object Name |
    ForEach-Object { "{0}: {1}" -f $_.Name, $_.Count }

@(
    "Reference migration completed: $(Get-Date -Format o)"
    "Source repository: $repoRoot"
    "Destination: $destinationRoot"
    "Files considered: $($report.Count)"
    ""
    $summary
    ""
    "Laptop originals were preserved. Review the CSV before deleting or moving any source files."
) | Set-Content -LiteralPath $summaryPath -Encoding UTF8 -WhatIf:$false

Write-Host ""
Write-Host "Migration report: $reportPath"
Write-Host "Summary:"
$summary | ForEach-Object { Write-Host "  $_" }
