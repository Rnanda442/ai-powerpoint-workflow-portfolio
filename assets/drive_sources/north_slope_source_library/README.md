# Source Library Index

This folder contains a lightweight index of the public/source-planning materials
organized for the Alaska North Slope gas hydrate project.

## Files

- `source_manifest.csv` lists the organized source files by category, source
  path, copied-library path, file size, and modification time.
- `source_index.md` summarizes the organized source groups and gives orientation
  snippets for later citation work.

## Local Full Library

The Google Drive file `North_Slope_Curated_Source_Library_UNCLASSIFIED.zip` has
been downloaded locally to this folder. The extracted working copy is under
`unclassified_local/source_library/`.

Those raw PDFs, DOCX files, and the zip archive are intentionally ignored by Git
because the archive is about 239 MB and one source PDF is listed at more than
100 MB, which is over GitHub's normal file-size limit. The Streamlit app uses
the tracked `source_manifest.csv` and `source_index.md` so the deployed site can
show the source-library index without trying to ship the full raw source files.

Extraction note: `02_usgs_and_field_reports/sir2012-5054_methods.pdf` reported
a decompression error during local extraction and should be refreshed from Drive
or the original source before citation work uses that specific PDF.

## How the Sources Are Used

The current project direction is not a general gas hydrate overview. The source
library is being used to support a future approved-data workflow:

1. measured wireline/core variables,
2. derived equations and physics features,
3. staged hydrate classification gates,
4. machine-learning features and validation,
5. results, uncertainty, and producibility discussion.

The broad manuscript remains useful as a synthesis/source accumulation, while
the classification-methods draft is the sharper project-facing document.

## What Is Not Included

The full source-library PDFs and DOCX files are not copied into this Git folder.
Several are large, and at least one exceeds GitHub's 100 MB file limit. Keep the
full source library locally or in an approved cloud/workspace storage location.

## Boundary

This index is for public-source planning only. Do not add classified,
restricted, credentialed, or approved-environment-only well-log data here.
