# LinkedIn / AI Portfolio Email Notes - June 11 Source Pass

Scope: Gmail threads and inline attachments used to improve the AI portfolio after the June 11 notes about LinkedIn, PowerPoint images, low-value visuals, and source-backed topic panels.

## Email Threads Used

| Date | Gmail message/thread | Subject | What changed in the repo |
|---|---|---|---|
| 2026-05-16 | `19e33480adbd4102` / `19e32ee33fb3e435` | `Rohan nanda Linkden post submission and Employee History` | Saved the DOE seal from the LinkedIn wording/media-check email and added it as North Slope media/provenance evidence. |
| 2026-06-11 | `19eb859ab4b15bd4` / `19eb84a3d4291ed9` | `ai portfolio updates 6/11` | Captured the instruction that ML architecture should show future use cases after the project, not overstate the current project. |
| 2026-06-11 | `19eb8bded6bdf5c7` / `19eb8ab1a3eb1352` | `AI powerpoint updates 6/11 new` | Saved three inline visual references and used them to drive AI workflow visual rows plus the ML diagram QA fix. |
| 2026-06-11 | `19eb912268782bbc` / `19eb8cfd642184d6` | `north slope of alaska powerpoint vizuals` | Saved eight inline images and wired the strongest North Slope/about references into the evidence manifests. |

## Local Assets Added

| Local asset | Use |
|---|---|
| `assets/gmail_updates/2026-06-11/linkedin_portfolio_notes/linkedin_doe_logo_inline.png` | DOE/MLEF media cue for North Slope LinkedIn wording and source/provenance context. |
| `assets/gmail_updates/2026-06-11/linkedin_portfolio_notes/visual_reference_01.png` | Action-sequence / encoder-decoder style reference for the AI workflow topic. |
| `assets/gmail_updates/2026-06-11/linkedin_portfolio_notes/visual_reference_02.png` | Random-forest visual reference for richer model-mechanics diagrams. |
| `assets/gmail_updates/2026-06-11/linkedin_portfolio_notes/visual_reference_03.png` | QA screenshot showing the stray literal closing tag in the ML diagram panel. |
| `assets/gmail_updates/2026-06-11/north_slope_powerpoint_visuals/north_slope_email_inline_01.png` | Well-log scaffold parameter cards with symbols, caveats, and locked targets. |
| `assets/gmail_updates/2026-06-11/north_slope_powerpoint_visuals/north_slope_email_inline_04.png` | Best full gas-hydrate intro slide with structural explorer context. |
| `assets/gmail_updates/2026-06-11/north_slope_powerpoint_visuals/north_slope_email_inline_07.png` | Strongest about/profile drawing reference. |
| `assets/gmail_updates/2026-06-11/north_slope_powerpoint_visuals/north_slope_email_inline_08.png` | North Slope title/about slide for profile framing. |

All twelve downloaded inline images are cataloged in `data/gmail_linkedin_source_inventory.csv`. The strongest public-facing rows are also wired into `data/project_visuals.csv` and `data/linkedin_evidence.csv`.

## Integration Decisions

- North Slope: keep the Drive-derived slide 7 decision map as the lead technical image, but add the June 11 gas-hydrate intro and well-log scaffold images to the source-backed topic strip and PowerPoint evidence panel.
- AI workflow: add the action-sequence and random-forest visual references as source-note assets for improving the diagram language, while keeping QGIS/task screenshots as the real project evidence.
- About/profile: use the drawing as the strongest public about visual; keep the World Cup and Spotify images cataloged as references with rights/context caveats.
- QA: sanitize short ML risk-gate text before rendering so HTML-like fragments such as a closing `div` tag cannot appear as visible panel copy.
