# Google Drive Reference Migration

This migration collects the laptop-only reference files recorded in the
portfolio inventories and copies them into:

`My Drive/Codex Project Reference Library`

It does not copy Git repositories, credentials, browser or Robinhood sessions,
or authorized DOE runtime folders. Laptop originals remain in place until the
migration report is reviewed.

## Before Running

1. Start Google Drive Desktop on the laptop and confirm `My Drive` is visible.
2. Pull the latest `ai-powerpoint-workflow-portfolio` repository.
3. Pull the latest `north-slope-gas-hydrates` repository.

## Preview

From PowerShell in `ai-powerpoint-workflow-portfolio`:

```powershell
.\scripts\migrate_references_to_google_drive.ps1 `
  -NorthSlopeRepo "C:\Users\gargi\Documents\Next level productivity\Gas hydrates unclassified info\north-slope-gas-hydrates" `
  -WhatIf
```

If Google Drive Desktop uses a nonstandard location, add:

```powershell
-DriveRoot "G:\My Drive"
```

## Run

```powershell
.\scripts\migrate_references_to_google_drive.ps1 `
  -NorthSlopeRepo "C:\Users\gargi\Documents\Next level productivity\Gas hydrates unclassified info\north-slope-gas-hydrates"
```

Files above 750 MB are skipped by default. After reviewing available Drive
space, include them with:

```powershell
-IncludeLargeFiles
```

## Safety Boundary

The script blocks:

- `.env`, token, credential, and Streamlit secret files
- `.git`, virtual environments, browser/auth caches, and `AppData`
- `data_runtime`, `outputs_runtime`, `models_runtime`, `logs_runtime`, and
  `configs_local`

Only public-source and project-synthesis North Slope references listed in the
repository manifest are considered. Controlled or authorized DOE files must
remain inside the approved OpenScienceLab environment.

## Reports

Each run creates CSV and text reports under:

`My Drive/Codex Project Reference Library/_migration_reports`

Statuses include `copied`, `already-present`, `missing`, `blocked`, and
`large-skipped`.
