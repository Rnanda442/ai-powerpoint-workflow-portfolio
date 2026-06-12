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
- Conceptual SVGs remain in the repo as architecture support, but they no longer lead the affected topic cards when a stronger local/Drive source image exists.
