# Source Dive: Topic Visual Replacements - 2026-06-12

This pass replaces low-value topic visuals with source-backed visuals already present in the local repo or verified through Drive deck/document reads. Rule used: each topic should lead with the strongest real project image first, then use architecture sketches as explanation.

## Source Map

| Topic | Lead visual now used | Local source | Drive / origin source | Why this visual leads |
|---|---|---|---|---|
| AI workflow / agent training | `assets/gmail_updates/2026-06-08/Screenshot 2026-05-17 233055.png` | Gmail screenshot package | Handshake/QGIS workflow evidence from profile/project folders | Real QGIS task state is stronger than an abstract agent diagram. |
| Thesis graph / critical minerals | `assets/project_visuals/linkedin_powerpoint_slides/ree_slide_map_spider_diagram.png` | Local REE slide export | Thesis Ch.1 Presentation, Drive deck `1gJeJLNLMWuDrnaPn9hUNj6kvtGLy8X93YEkALhroWLc` | Shows map context, REE element groupings, and spider-diagram evidence in one source image. |
| Processing earthquake | `assets/project_visuals/processing_earthquake_linkedin_poster.jpg` | Local LinkedIn poster frame plus `assets/videos/usgs_3d_globe_video.mp4` | Verified LinkedIn earthquake globe / Processing post | Keeps the origin creative-code project visible before feature-engineering diagrams. |
| Seismic / Pondicherry | `assets/project_visuals/pondicherry_near_offset_reannotated.png` | Local seismic figure export | Exploration Seismology Final Land Data, Drive deck `1DwJ6SYkXptmYenoTOY64plNg15kE57fknS9l7wm3sQo`; Pondicherry notebooks in `data/case_studies.csv` | Real interpreted seismic output is stronger than cloud-processing iconography. |
| North Slope energy / hydrate ML | `assets/drive_slide_thumbnails/north_slope_decision_map_slide.png` | Local Drive thumbnail and North Slope source library | FINAL 9-slide North Slope deck, slide 7, Drive deck `1F7XJXA5DKS6JfvzOSJ6BZNBgHIqg71dgXg9MxjZL0-o`; enriched North Slope ML document `1V3kZuu4euP6IhHwfnwscAh7RxDAqWMNu2tEf7wC_pW4` | Names intake, QC, feature store, split policy, target registry, model heads, leakage barrier, geologic review, and output. |
| Rock classification | `assets/project_visuals/rock_classification_slides/rock_raster_classification_map.png` | Local ADVGIS / rock-classification export | ADVGIS Final, Drive deck `1hhBL8bDuMQZgvZynY7m17sjDOzowtZk9fN_ZyHi5-ig`; critical-minerals PDF pages | Shows actual classification rasters; supporting images show classification schemas and property-comparison complexity. |
| SAGE / Valles field geophysics | `assets/project_visuals/powerpoint_sources/valles_sage/valles_sage_slide_095_1_depth_m.png` in the topic wall; field-acquisition, SeisBench, TEM profile, and TEM/MT location figures in the topic page | Local extraction from `VallesCaldera_SAGE22.pptx` | Drive PowerPoint `1YKArFK7CTDESPgT2De1jeiGCOKSuDdRk`; Near-Surface Dwellers deck remains supporting context | The card uses a compact resistivity-depth graph; the topic page now leads with actual SAGE PowerPoint figures rather than old generic thumbnails or Gmail screenshots. |
| Near-surface geophysics | `assets/project_visuals/powerpoint_sources/valles_sage/valles_sage_slide_074_1_tem_n_s_profile.png` | Local extraction from `VallesCaldera_SAGE22.pptx` | Drive PowerPoint `1YKArFK7CTDESPgT2De1jeiGCOKSuDdRk`; Near-Surface Dwellers deck `1bY4HCjuD-60DU6IMZXA_DAMeqza3Gq_xH_-Xd_-NwIA` confirms the shallow-method context | The topic now leads with a real SAGE TEM profile, with E/W profile and MT depth curves as companion source-strip evidence. |
| Hydrate ML architecture | `assets/drive_slide_thumbnails/north_slope_decision_map_slide.png` | Local North Slope slide thumbnail | FINAL 9-slide North Slope deck plus enriched ML document; Chong et al. 2022 gas-hydrate ANN paper | This topic is currently about North Slope hydrate model architecture, so the decision map is the correct lead. |
| Ambient noise | `assets/drive_slide_thumbnails/noisepy_monitoring_card.jpg` in the topic wall; full `noisepy_monitoring_slide.png` in evidence | Local NoisePy slide thumbnail | NoisePy Drive deck `1db8rT7vo8nEx8ZHyfIiOEqbIz4rheQdT8rVrc0B_BBs` | Real monitoring heatmap/CCF-style visual is stronger than the abstract processing poster; the card uses an optimized derivative for page weight. |
| Stock workflow | `assets/topic_visuals/app_pipeline.svg` in the topic wall; full `stock_all_tickers_chart.svg` in hero/evidence | Local Streamlit stock app export | `stockprediction2025` local project in `data/case_studies.csv` | The source chart is too large for the overview card, so the lightweight card shows the app-risk pipeline while the actual chart remains visible on the detail page. |
| SEM petrography | `assets/project_visuals/linkedin_powerpoint_slides/rock_thin_section_slide_01.jpg` | Local thin-section / petrography slide export | SEM petrography Drive deck `1vvMzqiRPkHiyPTyq6fZki04ZMUor7N1zR0SPebxmX_w` | The deck is about visible petrography labels vs interpreted proxy claims, so real microscopy/thin-section evidence should lead. |

## Additional Slide Candidates Found

Full manifest: `data/topic_slide_candidates.csv`. Visual review sheet: `assets/drive_slide_candidates/source_slide_candidate_contact_sheet.jpg`.

| Topic | Other useful slides found | Local candidate assets |
|---|---|---|
| AI workflow / agent training | No better Drive slide deck found; strongest sources remain QGIS task-state screenshots, classified GIS outputs, and Handshake task evidence. | `assets/gmail_updates/2026-06-08/Screenshot 2026-05-18 001002.png`, `Screenshot 2026-05-12 001652.png`, `Screenshot 2026-05-13 135958.png` |
| Thesis graph / critical minerals | Thesis Ch.1 slides 2-4 confirm knowledge graph views, node/edge structure, and results/implications. Local REE exports cover these well. | `ree_slide_system_overview.png`, `ree_slide_deposit_model.png`, `ree_slide_trace_element_model.png`, `ree_slide_summary_model.png` |
| Processing earthquake | No stronger slide source found. The next useful visual is the original Processing/LinkedIn video export, not another still slide. | `assets/project_visuals/processing_earthquake_linkedin_poster.jpg` |
| Seismic / Pondicherry | Exploration Seismology slides 8, 16, and 20 are now downloaded; slide 24 remains a candidate for a final migrated-stack summary. | `assets/drive_slide_candidates/seismic_slide_08_fold_maps.png`, `seismic_slide_16_fold_weighted_stack.png`, `seismic_slide_20_kirchhoff_migration.png` |
| North Slope energy / hydrate ML | The useful extras are slides 5, 6, and 8: feature equations, model ladder, and validation/masking review. | `north_slope_slide_05_equations_features.png`, `north_slope_slide_06_model_ladder.png`, `north_slope_slide_08_errors_validation.png` |
| Rock classification | ADVGIS slides 17-21 and 36-40 add classification-map depth; slide 17 is downloaded and now wired as supporting evidence. | `advgis_slide_17_classification_moho.png` plus existing rock classification exports |
| SAGE / Valles field geophysics | VallesCaldera_SAGE22 remains the active source: slides 50, 58, 74, 75, 79, and 95 are the useful extracted figures. | `assets/project_visuals/powerpoint_sources/valles_sage/*` |
| Near-surface geophysics | Near-Surface Dwellers is the richest new source. Slides 29, 39, 53, 90, 103, and 111 are all useful; 53, 90, 103, and 111 are the strongest. | `near_surface_slide_29_aerial_lines.png`, `near_surface_slide_53_west_fens_loupe_tem.png`, `near_surface_slide_90_x_z_inversion.png`, `near_surface_slide_103_ert_tem_overlap.png`, `near_surface_slide_111_integrated_interpretation.png` |
| Hydrate ML / Moho ML | ADVGIS slide 17 and slide 40 provide the best extra Moho/classification visuals; slides 10-15 are candidates if a depth-resampling sequence is needed. | `advgis_slide_17_classification_moho.png`, `advgis_slide_40_maps.png` |
| Ambient noise | NoisePy slides 2, 5, and 7 complete the source sequence before the existing monitoring slide: concept, workflow, cloud pipeline, monitoring output. | `noisepy_slide_02_window_cross_correlate.png`, `noisepy_slide_05_ambient_noise_workflow.png`, `noisepy_slide_07_cloud_native_workflow.png`, `noisepy_monitoring_slide.png` |
| Stock workflow | No Drive slide deck found; useful images come from the local Streamlit app/project exports and pipeline diagram. | `stock_all_tickers_chart.svg`, `stock_saved_data_chart.svg`, `app_pipeline.svg` |
| SEM petrography | SEM slides 3-5 are strong: detrital evidence, authigenic kaolinite, and kaolinite morphology/proxy caution. | `sem_slide_03_detrital_evidence.png`, `sem_slide_04_authigenic_kaolinite.png`, `sem_slide_05_kaolinite_morphology_caption.png` |

## June 11 Gmail / LinkedIn Portfolio Notes

Companion manifest: `docs/LINKEDIN_PORTFOLIO_EMAIL_NOTES_2026-06-11.md`.

| Source thread | Main usable additions | Repo integration |
|---|---|---|
| `AI powerpoint updates 6/11 new` | Action-sequence diagram reference, random-forest visual reference, and ML diagram QA screenshot. | Added to `data/gmail_linkedin_source_inventory.csv`, `data/project_visuals.csv`, and the AI workflow source-backed asset strip. |
| `north slope of alaska powerpoint vizuals` | Well-log scaffold cards, full gas-hydrate intro / structural explorer slide, DOE media cue, drawing/about references, and title/about slide. | Added to the North Slope PowerPoint evidence panel, source-backed topic strip, LinkedIn evidence manifest, and profile/about visual inventory. |
| `Rohan nanda Linkden post submission and Employee History` | DOE seal from the LinkedIn wording/media-check email. | Added as North Slope media/provenance evidence with an endorsement caveat. |

## Gmail LinkedIn Attachment Intake

Source batch: Gmail thread `19eb4f2c59250b2b`, subject `Ai portfolio changes new`, received June 10/11 2026. Local folder: `assets/gmail_updates/2026-06-11_linkedin_sources/`. Inventory: `data/gmail_linkedin_source_inventory.csv`. Visual review sheet: `assets/gmail_updates/2026-06-11_linkedin_sources/linkedin_email_attachment_contact_sheet.jpg`.

| Attachment | Topic use | Caveat |
|---|---|---|
| `Screenshot 2025-07-01 124154.png` | Seismic CMP/gather geometry evidence | Use as processing provenance; not a final interpreted result. |
| `Screenshot 2025-07-01 101358.png` | Seismic gather / trace evidence | Good for the pick-QA workflow, but needs crop and labeling before a polished panel. |
| `Screenshot 2025-07-12 194044.png` | Seismic or near-surface map/table context | Large source screenshot; keep exact origin visible until matched to a project paper or deck. |
| `Screenshot 2025-07-13 154603.png` | Near-surface line/index geometry | Useful for line intersections and coverage; still provenance evidence until origin is pinned down. |
| `Screenshot 2025-07-20 212113.png` | Agent-training task/rubric evidence | Training-task context only; not a completed autonomous-agent result. |
| `Screenshot 2025-07-21 160753.png` | Seismic log/station-output evidence | Supporting provenance image, not a scientific result by itself. |
| `Screenshot 2025-07-21 160808.png` | Seismic pick/review panel source | Supports the `PICK | CONFIDENCE | OVERRIDE` build queue item without claiming model accuracy. |
| `IMG_9800.jpg` | Seismic / large-data processing workflow evidence | Field-computer/photo evidence, not a result figure. |

Implementation note: the AI workflow, seismic, and near-surface source evidence strips now surface these recovered email attachments. The seismic topic also has a first builder-queue prototype for `PICK | CONFIDENCE | OVERRIDE`: a slider moves the pick marker, confidence band, and review decision beside recovered trace and map attachments. The app-level strip also states the caveat that recovered screenshots are provenance and review evidence unless a caption names them as final validated output.

Related June 11 inline-image batch: `docs/LINKEDIN_PORTFOLIO_EMAIL_NOTES_2026-06-11.md` tracks the AI portfolio visual references and North Slope PowerPoint notes from Gmail inline images. The relevant inline sources now used in the app are the action-sequence reference, random-forest classification schema, North Slope well-log scaffold, and North Slope hydrate/structural-explorer intro slide. Unrelated logo-only or pop-culture references remain in the source folder but are not promoted into topic evidence.

## Drive Reads Used

- `Thesis Ch.1 Presentation`: confirms Mountain Pass/Bayan Obo knowledge graph, node/edge structure, and system architecture slides.
- `FINAL 9-SLIDE REVISION North Slope Gas Hydrate ML Parameter Architecture Slides 2026-06-11`: confirms slide 4 parameter/caveat grid and slide 7 decision map.
- `ENRICHED ML PIPELINE North Slope Gas Hydrate Research Overview 2026-06-11`: confirms Chong et al. 2022, complete-well validation, target-leakage barrier, and CreditScoreV4/ML notes as reliability source.
- `ADVGIS Final`: confirms formation property tables, resistivity/density/P-wave/S-wave composites, and classification rasters.
- `NoisePy`: confirms windowing, cross-correlation, stacking, batch/cloud workflow, and monitoring slides.
- `SEM petrography`: confirms clay/kaolinite observation versus interpretation framing.
- `Near-Surface Dwellers Presentation`: confirms SAGE/GAGE field method sources: hammer seismic, ERT/TEM, line intersections, residual/DOI review, field errors, and possible units.
- `Exploration Seismology FInal Land data`: confirms seismic processing source slides: gain, bandpass, fold maps, VNMO, migration, and interpreted stack.

## Implementation Notes

- The app now applies `SOURCE_DIVE_VISUAL_OVERRIDES` after the older email visual overrides, so source-backed images win without deleting the earlier planning layer.
- `SOURCE_BACKED_TOPIC_ASSETS` was reordered for North Slope, Valles, and near-surface geophysics so the first visible source-strip cards match the best current evidence.
- `noisepy_monitoring_card.jpg` is an optimized derivative of the verified NoisePy slide thumbnail for the overview card only.
- Additional Drive thumbnails were downloaded to `assets/drive_slide_candidates/` and wired into the topic evidence panels where they add real source depth.
- June 11 Gmail/LinkedIn note images were downloaded to `assets/gmail_updates/2026-06-11/`, cataloged, and used to strengthen the AI workflow, North Slope, and profile/about evidence surfaces.
- Short ML risk-gate copy is now cleaned before rendering so source-note HTML fragments cannot appear as literal text in the diagram panel.
- Conceptual SVGs remain in the repo as architecture support, but they no longer lead the affected topic cards when a stronger local/Drive source image exists.
