# AI PowerPoint Workflow Storyboard

This project is a working folder for turning local AI-assisted work artifacts into
either a PowerPoint deck or a small website.

The current first pass focuses on a Streamlit storyboard site that can later be
expanded into:

- a portfolio-style website about AI research workflows
- a PowerPoint outline and exported `.pptx`
- a curated media folder with screenshots, videos, PDFs, notebooks, and code

## Strong Source Areas Found

- `C:\Users\gargi\Documents\Next level productivity\linkedin_media_handoff.md`
- `C:\Users\gargi\Downloads\stockprediction2025`
- `C:\Users\gargi\Documents\Next level productivity\Gas hydrates unclassified info\north-slope-gas-hydrates`
- `C:\Users\gargi\OneDrive\Documents\Processing`
- `C:\Users\gargi\Pictures\Screenshots`
- `C:\Users\gargi\Downloads\Profile.pdf`

## Run The Storyboard

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

## Project Files

- `app.py`: Streamlit storyboard site.
- `data/source_inventory.csv`: First-pass source inventory.
- `data/google_drive_inventory.csv`: First-pass Google Drive pull list with live links.
- `data/notebook_inventory.csv`: Local Jupyter notebook inventory with lightweight tags.
- `data/case_studies.csv`: Curated 10-15+ project board for the cleaner website view.
- `docs/narrative_outline.md`: Draft storyline for a deck or site.
- `assets/contact_sheets/`: Copied visual contact sheets for review.

## Safety Notes

Do not copy credential files, tokens, `.env` files, private account data, or
controlled research data into this project. The current inventory references
source paths but does not embed sensitive runtime files.
