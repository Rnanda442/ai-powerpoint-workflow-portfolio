# Website Visual Audit - 2026-06-09

## Fixed In This Pass

- North Slope topic card and topic hero no longer use the old Structural Explorer screenshot as the default project proof.
- Overview cards now have project-specific proof images for REE, Processing, North Slope, Valles, Moho ML, stock workflow, seismic, rock classification, and AI workflow.
- The site now uses a darker visual system so pages do not read as plain white Streamlit cards.
- The North Slope topic page now shows a local source-library index summary and download link from `assets/drive_sources/north_slope_source_library/`.

## Problems Found

- The old `north_slope_3d_streamlit_plotly_map.png` was acting like generic evidence when the site needed project-specific screenshots.
- Several topic pages still rely on abstract SVG posters before showing real evidence.
- Some evidence rows still point to `C:\Users\gargi\...` source paths from the laptop. Those paths are not directly available on this desktop unless copied from Drive or another local repo.
- The North Slope source-library manifest exists locally, but most actual PDF/DOCX source files listed in that manifest are not yet copied into this portfolio repo.
- Google Drive search can find high-level Docs/Slides, but the full "North Slope curated source library" folder has not been identified by URL or exact accessible folder name.

## Replacement Priorities

1. Replace every abstract-only topic card with one strong real image plus one small concept layer.
2. Keep the Structural Explorer screenshot only on the North Slope Structural Explorer page or North Slope-specific evidence sections.
3. Copy the full North Slope curated source-library PDFs/DOCX files locally once the Drive folder is identified.
4. Add stronger first-screen visuals for Processing video, Valles field geophysics, Moho ML, and stock dashboard.
5. Remove or rewrite any caption that implies a screenshot proves a project it does not actually belong to.

## Drive Access Notes

- `data/google_drive_inventory.csv` contains accessible links for several Docs and Slides.
- Some native Google exports are blocked by Drive permissions, even when text fetch works.
- Direct unauthenticated Google export URLs return `401 Unauthorized`.
- The next reliable step is to provide or locate the exact Google Drive folder URL for the North Slope source library, then export/download each accessible file into `assets/drive_sources/north_slope_source_library/files/`.
