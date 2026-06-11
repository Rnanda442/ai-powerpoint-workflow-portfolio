# ML Topic Improvement Plan - June 11, 2026

This document turns the two Gmail instruction threads into a section-by-section and topic-by-topic implementation plan for the Streamlit portfolio. The goal is not to add generic AI language. The goal is to make every topic show:

- the real example already in the portfolio
- the source images or slide evidence that should be visible in-page
- a new use case that extends the example beyond the original project
- a visual concept that can be built in Streamlit, Processing, SVG, or a slide deck
- an ML pipeline or architecture flow using the actual ML-source vocabulary
- the error, leakage, uncertainty, or validation gates that make the idea credible

## ML Sources To Implement More Heavily

These sources should become the technical vocabulary behind the topic pages and diagrams.

1. GUI agents survey
   - Use for: screenshot/prompt-to-Codex topic, supervised agent traces, action histories, tool-use trajectories, environment state, human feedback, task replay.
   - Website language to add: "action trace", "state observation", "GUI grounding", "instruction following", "trajectory supervision", "held-out software task".

2. ADEPT scientific workflow agents
   - Use for: cloud workspaces, scientific notebooks, agent execution of research steps, phone-to-cloud workflows.
   - Website language to add: "scientific workflow agent", "task graph", "artifact handoff", "runtime provenance", "human checkpoint".

3. Geoscience knowledge graph pipeline
   - Use for: REE/critical minerals graph topic, source-backed edge types, graph validation, entity extraction.
   - Website language to add: "entity extraction", "relationship ranking", "ontology", "source-backed edge", "inferred edge", "schema audit".

4. Critical minerals GraphRAG
   - Use for: knowledge graph topic, thesis/REE topic, critical-mineral reasoning, document-to-graph retrieval.
   - Website language to add: "retrieval augmented graph", "source chunk", "graph query", "ranked relationship", "human edge review".

5. GNN mineral prospectivity mapping
   - Use for: critical minerals, satellite rock classification, resource maps, graph features over geologic regions.
   - Website language to add: "node features", "spatial edge", "prospectivity score", "message passing", "graph leakage".

6. Spatial cross-validation for GeoAI
   - Use for: satellite classification, Valles/SAGE, near-surface methods, North Slope maps.
   - Website language to add: "spatial block split", "leave-area-out validation", "spatial autocorrelation", "mixed-pixel error", "domain shift".

7. SeisLM seismic waveform foundation model
   - Use for: large seismic processing, ambient noise, waveform QA.
   - Website language to add: "foundation waveform embedding", "pretrained seismic representation", "phase-pick uncertainty", "station metadata".

8. Seismic foundation model
   - Use for: seismic processing, promptable interpretation, large-scale seismic review.
   - Website language to add: "pretraining corpus", "transfer learning", "seismic representation", "fine-tuned task head".

9. Promptable seismic geobody model
   - Use for: seismic images, geobody interpretation, human-in-the-loop prompts.
   - Website language to add: "promptable segmentation", "geobody mask", "interactive correction", "interpretation uncertainty".

10. Physics-informed ML for subsurface energy
    - Use for: North Slope, hydrate prediction, reservoir/energy workflows.
    - Website language to add: "physics constraint", "mass/energy consistency", "well-log feature transform", "uncertainty calibration".

11. Gas hydrate well-log ML
    - Use for: hydrate architecture topic, North Slope ML diagram, well-held-out validation.
    - Website language to add: "hydrate occurrence head", "saturation regression head", "well-held-out split", "calibration", "abstention".

12. DOE AI for Energy report
    - Use for: energy crisis framing, scientific productivity, public data workspaces, agent-supported workflows.
    - Website language to add: "energy decision support", "human oversight", "scientific productivity", "data governance".

13. USGS Earth MRI
    - Use for: critical minerals, public-source geoscience, map/source library examples.
    - Website language to add: "public geoscience layer", "mineral systems", "source provenance", "survey coverage".

## Site-Wide Section Plan

### Start Page

Current purpose: topic wall that invites the viewer into the AI workflow think tank.

Improvement:
- Add a small "ML backbone" legend visible above or beside the topic wall: Agent traces, GraphRAG, GeoAI spatial CV, seismic foundation models, physics-informed ML, leakage-safe validation.
- Add a route overlay that visually connects topics by shared ML risk:
  - screenshots -> agent traces -> workflow execution
  - papers/slides -> GraphRAG -> knowledge graph
  - maps/rasters -> GeoAI -> spatial CV
  - waveforms/noise -> seismic foundation models -> monitoring
  - wells/logs -> physics-informed ML -> leakage gates
- Keep the copy short. The first screen should say that the site is about converting real project evidence into future AI/ML systems.

Visual to build:
- A thin Processing-style animated route layer behind the cards. Dots should move from source type to ML method to validation gate. Each route should land on one of the topic cards.

Error/validation to show:
- A small "trust gate" icon for every route: provenance, leakage, uncertainty, spatial split, human review.

### Topics Section

Current purpose: each topic page contains the real example, the AI use, source images, and a pipeline contract.

Improvement:
- Standardize every topic page into the same reading order:
  1. question
  2. current example
  3. source image deck
  4. new use case
  5. visual concept
  6. ML architecture
  7. error gates
  8. audience challenge
- Move the pipeline contract higher on each page so the ML architecture is not buried under downstream detail.
- Add a "Use outside geoscience" mini-panel to every topic with banking, startup, agriculture, commerce, public-sector, or energy examples where relevant.

Visual to build:
- One consistent "ML architecture card" component with left-to-right lanes: Inputs, Feature Store, Model Layer, Validation Gates, Human Review, Output.

Error/validation to show:
- The validation lane should be red or amber when leakage, weak labels, missing provenance, spatial autocorrelation, or model drift can break the workflow.

### Interactives / Structural Explorer

Current purpose: shows the North Slope work and geoscience interactivity.

Improvement:
- Make the Structural Explorer the proof that public-source data can become a safe workbench.
- Add a "public-safe ML scaffold" side panel that explains what can be scraped and shown publicly versus what must remain restricted.
- Tie the North Slope view to the hydrate ML architecture topic: public layers are not enough for prediction, but they prepare the feature and provenance context.

Visual to build:
- A split view: left map/layers, right ML scaffold. The scaffold should show public source metadata, coordinate system, source trust, well skeleton, and candidate feature groups.

Error/validation to show:
- CRS mismatch, stale public source, restricted-data leak, missing formation tag, and false hydrate inference from map-only context.

### Visual Lab / Processing

Current purpose: shows motion and Processing language but needs more finished sketches.

Improvement:
- Treat Processing as the "visual ML thinking lab." It should not only make decorative visuals. It should show how variables become features, how model outputs move, and where uncertainty appears.
- Build small Processing sketches for the most important ML pipeline moments:
  - action traces becoming supervised agent examples
  - GraphRAG edges growing from source chunks
  - earthquake 3D points flattening into time-window features
  - seismic files entering a cloud run
  - station-pair correlations stacking over time
  - hydrate feature gates blocking leakage

Visual to build:
- Each Processing sketch should have a source lane, feature lane, model lane, error lane, and output lane. The animation should make error visible instead of hiding it.

Error/validation to show:
- Overfit paths should get blocked, uncertain predictions should flicker or fade, and human-review points should pause the animation.

### About / Contact

Current purpose: explains the work and lets viewers share ideas.

Improvement:
- Add a short "What I am testing" section: how real geoscience, AI workflows, and ML architecture diagrams can help teams move from scattered evidence to reviewable decisions.
- Add the rule: every AI claim must show source, pipeline, and validation.

Visual to build:
- A compact "source -> pipeline -> validation -> decision" diagram.

Error/validation to show:
- Show "unsupported claim" as a blocked output.

### Build Room

Current purpose: internal source/control room.

Improvement:
- Add a "ML Source Implementation Tracker" table:
  - source name
  - pages using it
  - diagram vocabulary added
  - visual still needed
  - validation/error gate added
- Add a "Gmail Instruction Coverage" checklist so new emails can be converted into concrete tasks.

Visual to build:
- A matrix where topics are rows and ML sources are columns. Filled cells should link to source images or pipeline panels.

Error/validation to show:
- Mark gaps where a topic has a visual but no ML source, or an ML pipeline but no visible source image.

## Topic-by-Topic Improvement Plan

### 1. Will Screenshots And ChatGPT Prompting Be Replaced By Codex?

Current example:
- Human reads a prompt and rubric, executes the work in a screen-recorded software environment, and produces projects in tools like QGIS, ParaView, 3D Slicer, KiCad, notebooks, or geoscience workspaces.
- The site now has prompt/rubric screenshots and a supervised agent-training pipeline, but the next pass should make the architecture more specific.

New use cases:
- Energy: an agent executes repeated public-data preparation tasks for energy-security project screening while a geologist reviews final maps.
- Agriculture: an agent runs repeated GIS crop-stress workflows from satellite data, then creates field-ready maps for agronomists.
- Commerce/startups: an agent takes founder prompts, opens app builders, creates dashboards, runs tests, and logs failures for review.
- Manufacturing: an agent executes inspection workflows in CAD/KiCad-like environments and flags uncertain steps instead of silently continuing.

Visual to build:
- "Trace Factory" diagram. Left side: prompt, rubric, screen recording, file tree, clicks, keyboard actions. Middle: action trace encoder, environment-state store, rubric labeler, failure labeler. Right side: agent policy, tool planner, replay simulator, human review queue, accepted project output.
- Processing sketch: cursor paths become colored traces. Green segments are successful actions, red segments are failed or corrected actions, blue segments are human decisions.

ML pipeline and architecture:
1. Ingest screen recordings, prompts, rubrics, file snapshots, terminal logs, and final artifacts.
2. Segment video into action traces: observe state, choose action, execute, check result.
3. Convert traces into supervised examples using rubric labels and human correction labels.
4. Train or fine-tune a GUI/action model with state observation, tool-use trajectory, and instruction-following supervision.
5. Add retrieval from previous project examples so the agent can reuse patterns without memorizing one task.
6. Evaluate on held-out software tasks: unseen prompts, unseen file structures, and unseen project goals.
7. Deploy only with a human checkpoint for file writes, external actions, or uncertain execution.

ML source implementation:
- GUI agents survey: action traces, GUI grounding, instruction following, trajectory supervision.
- ADEPT scientific workflow agents: scientific task graph, artifact handoff, runtime provenance.
- DOE AI for Energy: human oversight and energy decision support.

Error and validation gates:
- Shortcut memorization: agent learns the screen layout instead of task logic.
- Missing state: video does not capture hidden files, environment variables, or data paths.
- Unsafe action: agent deletes, uploads, or overwrites without approval.
- Rubric ambiguity: labels are inconsistent across reviewers.
- Evaluation rule: use held-out tasks and require replay success, not just a good final screenshot.

Website tasks:
- Add a "trajectory supervision" block to the current ML contract.
- Add a visual timeline showing supervised agent training from hundreds of project videos.
- Add a cross-sector panel with energy, agriculture, commerce, and manufacturing examples.

### 2. Knowledge Graphs And Diagrams Built Using AI: Are They The Next Way To Understand Project Architectures?

Current example:
- REE and critical-mineral work: Mt Pass, Bayan Obo, mineral relationships, geochemical diagrams, thesis slides, and AI-assisted explanation of how variables relate.
- The site now shows REE visuals and Critical Minerals PDF heatmaps, but the next pass should make graph reasoning and architecture diagrams the core visual.

New use cases:
- Banking: build a graph of risk variables, borrowers, sectors, collateral, macro signals, and evidence sources so analysts can debate why a risk score changed.
- Startup strategy: connect customer pain points, product features, launch channels, user feedback, and engineering dependencies.
- Marketing: connect audience segments, content topics, campaigns, creative assets, conversion events, and attribution uncertainty.
- Energy: connect public geology, reports, minerals, formations, infrastructure, and policy constraints.

Visual to build:
- Replace straight-line block graphics with a circular AI/ML hub. Left vertical blocks: tables/CSVs, questions/projects, drawings/ideas. Center: AI/ML circle. Right vertical blocks: knowledge graph, ML architecture diagram, scientific drawing.
- Processing sketch: source nodes orbit into the AI/ML circle, then edges grow outward with different styles for source-backed, AI-suggested, and human-interpreted links.

ML pipeline and architecture:
1. Ingest papers, slide text, CSV tables, map labels, drawings, and source notes.
2. Extract entities: mineral, host rock, deposit, process, location, age, evidence source.
3. Normalize synonyms and create an ontology so "REE deposit", "rare earth element deposit", and site-specific labels do not split into duplicate nodes.
4. Classify edge types: observed, inferred, analog, conceptual, or AI-suggested.
5. Rank relationships with GraphRAG retrieval and source-weighted confidence.
6. Add a graph ML layer for prospectivity or relationship prediction only after source-backed edges are separated from inferred edges.
7. Render graph, architecture diagram, and scientific drawing as three synchronized views.

ML source implementation:
- Geoscience knowledge graph pipeline: entity extraction, ontology, source-backed edges.
- Critical minerals GraphRAG: graph retrieval and ranked relationship evidence.
- GNN mineral prospectivity mapping: node features, message passing, prospectivity score.
- USGS Earth MRI: public mineral systems and survey layers.

Error and validation gates:
- Edge hallucination: AI creates a relationship that has no source support.
- Synonym duplication: one mineral or formation becomes multiple nodes.
- Overweighted diagram: a visually attractive edge appears stronger than the evidence.
- Graph leakage: prospectivity labels leak through spatial or literature-derived features.
- Evaluation rule: edge audit by human, source trace visible on click, and separate styling for observed versus inferred relationships.

Website tasks:
- Add a "graph edge legend" near the first visual.
- Add sector examples with short visual thumbnails.
- Add a graph query example: "Why does this mineral associate with this host rock?"

### 3. Can We Use AI To Visualize Data Into New Variables For Prediction Models?

Current example:
- The earthquake Processing sketch converted event locations, magnitude, depth, and time into a 3D globe and sound-mapped experience.
- The key idea is not prediction from a globe. The key idea is feature transformation: a 3D/time experience can be converted into simpler time-window variables for ML.

New use cases:
- Finance: turn many price series into rolling window features and sound/visual anomaly cues before testing forecasting models.
- Supply chain: convert shipment locations and delays into time-window congestion features.
- Health operations: convert patient flow events into time-window pressure features for staffing.
- Agriculture: convert satellite change over time into crop-stress windows.

Visual to build:
- "3D to 2D Feature Converter" diagram. Left: 3D globe with event points and sound wave. Middle: flattening lens. Right: time-window table with event count, depth bins, magnitude bins, cluster density, lagged windows.
- Processing sketch: points orbit on a globe, then slide into a horizontal feature timeline. Each time window becomes a model-ready row.

ML pipeline and architecture:
1. Ingest event catalog with latitude, longitude, depth, magnitude, and timestamp.
2. Clean coordinates and timestamps; remove duplicate or bad events.
3. Convert events into windows by region and time.
4. Build derived features: counts, magnitude distribution, depth distribution, cluster density, change rate, lagged history.
5. Train baseline regression or classification models on past windows.
6. Compare nonlinear challenger models only after baseline and validation are clear.
7. Output feature visualization, residual plot, uncertainty, and "not a forecast" warning where needed.

ML source implementation:
- Spatial cross-validation for GeoAI: region-window validation and spatial leakage control.
- SeisLM / seismic foundation thinking: pretrained representations for waveform-like event sequences can inspire embeddings, but only if source data supports it.
- DOE AI for Energy: explainable decision support, not unsupported prediction claims.

Error and validation gates:
- Look-ahead leakage: future events included in training windows.
- Visual overread: clusters on the globe interpreted as prediction without a model.
- Imbalanced rare events: strong earthquakes are too rare for naive metrics.
- Spatial autocorrelation: nearby windows make random splits overoptimistic.
- Evaluation rule: train on past, test on later windows or leave regions out.

Website tasks:
- Rewrite the topic as feature engineering, not earthquake forecasting.
- Add a diagram of original variables -> transformed variables -> model rows.
- Add examples from finance, supply chain, agriculture, and health operations.

### 4. Large Data Processing Streamlined With AI

Current example:
- Seismic and cloud data workflows: Codex, GitHub, OpenScienceLab/ASF cloud, notebooks, field-computer screenshots, and scientific artifact review.
- The site now includes `IMG_9800.jpg` and local seismic images, but the next pass should make the cloud architecture sharper.

New use cases:
- Energy: process seismic and satellite datasets in cloud workspaces while committing outputs to GitHub.
- Agriculture: process large satellite scenes for crop monitoring without waiting at a desktop.
- Disaster response: process SAR/flood/landslide scenes from a phone-triggered cloud workflow.
- Enterprise analytics: run large ETL jobs with agent-generated QA reports and reproducible commits.

Visual to build:
- "Phone-to-Cloud Scientific Run" architecture. Phone prompt -> Codex task -> GitHub branch -> cloud workspace -> data mount -> notebook/run container -> artifact store -> QA panel -> pull request.
- Processing sketch: large files fall into a cloud node, branch into notebook runs, then outputs pass through a QA gate before a GitHub commit appears.

ML pipeline and architecture:
1. Register dataset metadata: source, size, sensor, station/scene, CRS, time coverage, license.
2. Stage data in a cloud workspace with immutable run IDs.
3. Use agent-generated task graph for download, preprocessing, model inference, visualization, and artifact export.
4. Run foundation-model or task-model inference where appropriate: waveform embeddings, phase picking, geobody segmentation, or satellite feature extraction.
5. Store run logs, parameters, errors, and sample outputs.
6. Generate QA summary and human-review checklist.
7. Commit code, parameter file, and reviewed outputs to GitHub.

ML source implementation:
- ADEPT scientific workflow agents: task graph, runtime provenance, artifact handoff.
- SeisLM seismic waveform foundation model: waveform embeddings and phase-pick uncertainty.
- Seismic foundation model: pretrained representation and task heads.
- Promptable seismic geobody model: promptable segmentation and human correction.

Error and validation gates:
- Environment drift: notebook works once but not later.
- Silent missing files: model runs on partial data.
- Wrong station metadata or CRS: output appears valid but is spatially wrong.
- Foundation-model transfer error: pretrained model is used outside its domain.
- QA rule: every run needs a manifest with data source, parameters, output sample, warnings, and reviewer sign-off.

Website tasks:
- Add cloud architecture visual near the top.
- Use `IMG_9800.jpg` as the field-computer proof image and explain it.
- Add "large-data error constraints" panel: missingness, metadata, environment, cost, domain shift.

### 5. Using AI For Web Scraping And Public Energy-Data Workspaces

Current example:
- North Slope public-source project: public maps, shapefiles, reports, source libraries, Streamlit app, and well scaffold concept.
- The site now uses the newest North Slope deck images and public map evidence. The next pass should make the public-safe boundary and scraper architecture more explicit.

New use cases:
- Energy: continuously scrape public geology, permits, infrastructure, and reports into one review workspace.
- Banking/insurance: scrape public risk, property, climate, and infrastructure data into due-diligence dashboards.
- Agriculture: scrape soil, weather, crop, water, and satellite sources into farm decision workspaces.
- Public sector: collect grants, surveys, maps, and infrastructure records into a searchable source atlas.

Visual to build:
- "Public Source Harvester" diagram. Public maps/PDFs/shapefiles/APIs -> scraper/API collector -> source registry -> schema matcher -> spatial aligner -> public-safe well scaffold -> review workspace.
- Show a red wall between public-safe features and restricted/private well data.

ML pipeline and architecture:
1. Discover public sources using search, APIs, public portals, and known agency sites.
2. Store source metadata: URL, license, date, coordinate system, coverage, trust score.
3. Parse files into structured layers: shapefiles, tables, PDF text, image thumbnails.
4. Use schema matching to standardize formation names, locations, units, and source categories.
5. Spatially align layers and build public-safe feature scaffolds.
6. Rank sources by relevance and trust for the user's question.
7. Output a Streamlit workspace with provenance-first visuals and human review notes.

ML source implementation:
- DOE AI for Energy: data governance and human oversight.
- USGS Earth MRI: public geoscience source model.
- Spatial cross-validation for GeoAI: spatial splitting and source-area bias.
- Physics-informed ML for subsurface energy: avoid making physical claims from scraped context alone.

Error and validation gates:
- Restricted-data leak: private well data accidentally mixed into public view.
- CRS mismatch: layers align visually but not correctly.
- Stale source: old public data treated as current.
- Source hallucination: scraper invents metadata or misses license constraints.
- Validation rule: source registry must show public status, date, CRS, and review flag before a layer is trusted.

Website tasks:
- Add the well scaffold view directly in the topic if available as a source image.
- Add a public-safe boundary diagram.
- Add cross-industry scraper examples.

### 6. Classification Of Rock Types Using Satellite Variables And How AI Can Make This More Accurate

Current example:
- ADV GIS rock classification with satellite variables, plus Critical Minerals PDF graphs showing complex geochemical/property relationships.
- The key distinction: satellite/ADV GIS variables drive classification; geochemical spider diagrams and heatmaps explain complexity and validation context.

New use cases:
- Mining/exploration: classify lithology or alteration zones from satellite and DEM variables.
- Agriculture: classify soil or surface-condition zones from spectral and terrain variables.
- Construction: screen aggregate or rock-material zones before field visits.
- Environmental monitoring: detect land-cover or mine-disturbance classes with uncertainty.

Visual to build:
- "Satellite Variable Classifier" architecture. Satellite bands, DEM derivatives, texture, slope, training polygons -> spatial feature store -> model candidates -> uncertainty map -> field-review queue.
- Side panel: Critical Minerals PDF heatmaps and trend comparison explain why rock-property labels are not simple.

ML pipeline and architecture:
1. Ingest satellite bands, DEM, derived indices, texture, slope, aspect, and mapped geologic context.
2. Clean and align rasters to one CRS and resolution.
3. Build labels from reviewed maps or training polygons.
4. Split by spatial blocks or leave-area-out, not random pixels.
5. Train baseline, tree/boosted, or spatial/GNN-informed models depending on data structure.
6. Generate class probability, uncertainty, and mixed-pixel flags.
7. Send uncertain or high-impact zones to field or expert review.

ML source implementation:
- Spatial cross-validation for GeoAI: spatial block split and autocorrelation.
- GNN mineral prospectivity mapping: graph of neighboring cells, geologic units, and prospectivity.
- USGS Earth MRI: public survey and mineral-system framing.
- Critical minerals PDF: measurement condition, heatmaps, trend comparisons, and property correlation.

Error and validation gates:
- Random-pixel leakage: neighboring pixels from the same area appear in train and test.
- Mixed-pixel error: one pixel contains multiple rock types or surface covers.
- Label noise: map labels are generalized or wrong at pixel scale.
- Domain shift: classifier trained in one region fails in another.
- Validation rule: report spatial CV, class imbalance, uncertainty, and field-review needs.

Website tasks:
- Place ADV GIS satellite-variable source images first.
- Use Critical Minerals PDF pages as "complexity evidence", not hidden inputs.
- Add a visual split showing model input versus supporting interpretation evidence.

### 7. How Should AI Compare Imperfect Geophysical Surveys Without Flattening Uncertainty?

Current example:
- SAGE/Valles geophysical surveys: gravity, EM, ERT/TEM, seismic, maps, possible units, and field interpretation.
- The page should never imply that AI merges methods into one perfect answer. It should show disagreement.

New use cases:
- Geothermal exploration: compare gravity, MT, EM, seismic, and geology to rank drilling uncertainty.
- Infrastructure: compare geophysics, boreholes, utility maps, and field notes for corridor planning.
- Water resources: compare ERT, TEM, wells, and geology for aquifer screening.
- Environmental remediation: compare surveys to identify uncertain contamination pathways.

Visual to build:
- "Disagreement Board" visual. Each method has a lane: gravity, EM/TEM, ERT, seismic, geology. Intersections glow when methods agree and become striped when they conflict.
- Processing sketch: layers slide together but conflict zones remain visible instead of being averaged away.

ML pipeline and architecture:
1. Ingest method outputs and metadata: survey geometry, acquisition settings, processing assumptions, signal strength.
2. Register each method to a shared spatial frame.
3. Extract method-specific features and uncertainty scores.
4. Build agreement/conflict labels at intersections or grid cells.
5. Use a model only to rank review priority, not to erase disagreement.
6. Output a review board with method confidence, conflict type, and recommended next observation.

ML source implementation:
- Spatial cross-validation for GeoAI: location-aware validation.
- Physics-informed ML for subsurface energy: method physics and constraints.
- Seismic foundation model sources where seismic traces or sections are included.
- GNN mineral prospectivity mapping where relationships between units and survey responses become graph features.

Error and validation gates:
- Misregistration: lines and grids do not align.
- Method physics ignored: AI treats ERT and gravity as interchangeable images.
- Acquisition artifact: noise becomes a false geologic boundary.
- False consensus: averaging methods hides real conflict.
- Validation rule: expert review must see conflict zones and method-specific uncertainty.

Website tasks:
- Replace any generic/person image with real SAGE/Near-Surface visuals.
- Add an uncertainty legend and method-lane visual.
- Add examples from geothermal, infrastructure, water, and remediation.

### 8. Can AI Compare Shallow Geophysical Methods Without Erasing Disagreement?

Current example:
- Near-Surface Dwellers deck: fen context, hammer seismic, transient EM, ERT, possible units, and line intersections.
- This is the shallow-field version of the Valles problem, with a stronger focus on line intersections and field-scale disagreement.

New use cases:
- Wetland monitoring: combine shallow geophysics and field notes to track hydrologic change.
- Utility siting: compare shallow methods before digging.
- Farm drainage: combine ERT and shallow seismic for soil/water structure.
- Archaeology or cultural-resource screening: compare non-invasive surveys with confidence limits.

Visual to build:
- "Fen Method Fusion" cross-section. Hammer seismic velocity, ERT resistivity, TEM conductivity, possible units, and field notes each appear as layers. Agreement zones glow. Conflict zones stay striped and labeled.
- Processing sketch: line intersections pulse when methods agree; red hatch marks appear when one method contradicts another.

ML pipeline and architecture:
1. Crop and register source slides, field line maps, and method panels.
2. Extract or manually label line geometry, method type, signal interval, possible unit, and field-note context.
3. Build a method-feature table: velocity, resistivity, conductivity, depth, line ID, uncertainty.
4. Train or rule-rank agreement/conflict zones only after method physics is encoded.
5. Output review targets rather than final units.
6. Store human decisions so future field projects learn which conflicts mattered.

ML source implementation:
- Spatial cross-validation for GeoAI: line-aware validation and leave-line-out testing.
- Physics-informed ML for subsurface energy: method constraints and physical plausibility.
- ADEPT scientific workflow agents: artifact handoff from slide/source to review workspace.

Error and validation gates:
- Wrong line intersection: methods appear to disagree because geometry is wrong.
- Field-note loss: context is dropped during extraction.
- Clean overlay overclaim: model makes a smooth map that hides method limits.
- Unit label drift: possible unit becomes asserted unit.
- Validation rule: every output zone must show method evidence, conflict status, and human review.

Website tasks:
- Add more actual Near-Surface Dwellers/SAGE images from the large deck.
- Add a shallow-method pipeline diagram using velocity, resistivity, conductivity, line, unit, and field-note features.
- Add a review target output instead of a "final answer" output.

### 9. What ML Architecture Predicts Hydrates Without Leakage?

Current example:
- North Slope hydrate ML architecture: newest slide deck, log-derived features, resistivity, NMR, sonic, density, GR, core/PT caveats, leakage barrier, and complete-well validation.
- This is the strongest candidate for a real ML architecture page and should be treated as the backbone example for serious ML audiences.

New use cases:
- Carbon storage: predict reservoir suitability with physics constraints and well-held-out validation.
- Geothermal: rank intervals where temperature, permeability, and structure are promising.
- Mining/exploration: classify mineralized intervals from logs, geochemistry, and geology while preventing spatial leakage.
- Environmental monitoring: classify risk intervals from borehole and geophysical logs.

Visual to build:
- "Leakage-Safe Hydrate Architecture" diagram with columns:
  1. raw logs and metadata
  2. QC gates
  3. training-well feature transforms
  4. feature store
  5. split policy
  6. occurrence classifier head
  7. saturation regression head
  8. calibration/abstention
  9. geologic review
  10. public-safe output
- Add a red leakage barrier between target labels and feature engineering.

ML pipeline and architecture:
1. Ingest logs: resistivity, density, sonic, shear sonic if available, GR, caliper, NMR, core intervals, pressure-temperature context, formation tops.
2. Run QC: depth alignment, missing curves, bad hole flags, caliper washout, unit normalization.
3. Fit feature transforms only on training wells: Vsh, phi_den, Vp/Vs, acoustic impedance, lambda-rho, mu-rho, H_proxy, NMR separation.
4. Split by complete wells or geologic areas, never random depth rows.
5. Train baseline models, tree/boosted models, and ANN challengers for two heads: hydrate occurrence and saturation/regression.
6. Calibrate probabilities and define abstention rules for uncertain intervals.
7. Evaluate occurrence with precision/recall/F1 and saturation with MAE/RMSE/R2.
8. Send uncertain or high-value intervals to geologic review.

ML source implementation:
- Gas hydrate well-log ML: hydrate occurrence, saturation regression, well-log features.
- Physics-informed ML for subsurface energy: physical plausibility and feature constraints.
- Spatial cross-validation for GeoAI: well-held-out and area-held-out validation.
- DOE AI for Energy: decision support and human oversight.

Error and validation gates:
- Target leakage: labels or post-drilling interpretations enter feature generation.
- Random depth-row overfit: same well appears in train and test.
- Missing NMR/shear sonic: model treats unavailable high-value features as universal.
- Gas/ice/cement lookalike: non-hydrate responses mimic hydrate signatures.
- Calibration error: probability is overconfident even when ranking is good.
- Validation rule: complete-well split, leakage audit, calibration plot, abstention threshold, and geologist sign-off.

Website tasks:
- Make this topic's architecture diagram larger and more central.
- Add a metrics strip: occurrence metrics, saturation metrics, calibration, abstention.
- Add an "error gallery" for leakage, missing logs, and lookalike signatures.

### 10. Which Ambient-Noise Correlations Are Real Enough To Monitor?

Current example:
- NoisePy slide deck and continuous seismic monitoring workflow: station pairs, cross-correlation functions, stacking, heatmaps, compute logs, and monitoring outputs.
- The site now embeds a NoisePy slide image, but the next pass should explain how AI speeds monitoring without overclaiming weak correlations.

New use cases:
- Volcano monitoring: track velocity changes or correlation shifts across station pairs.
- Infrastructure: monitor bridges, tunnels, or urban vibration fields.
- Industrial operations: detect equipment or site vibration anomalies over time.
- City-scale sensing: monitor subsurface or traffic-induced noise patterns.

Visual to build:
- "Ambient Noise Monitoring Ladder" diagram. Continuous records -> windows -> preprocessing -> station-pair CCF -> stable stack -> change metric -> alert triage -> human review.
- Processing sketch: station pairs draw lines across a map; stable correlations become solid, unstable correlations flicker, and alerts enter a review queue.

ML pipeline and architecture:
1. Ingest continuous station data and station metadata.
2. Window records and remove bad windows using QC features.
3. Preprocess traces and compute cross-correlation functions by station pair.
4. Stack stable windows and track lag-time or waveform changes.
5. Use anomaly detection or representation learning to triage station pairs.
6. Separate seasonal/instrument changes from possible subsurface signals.
7. Output monitoring heatmap, parameter log, and alert explanation.

ML source implementation:
- SeisLM: waveform embeddings and seismic representation learning.
- Seismic foundation model: transfer learning for waveform tasks.
- ADEPT scientific workflow agents: continuous workflow and runtime provenance.
- Spatial cross-validation for GeoAI: station/region-aware validation.

Error and validation gates:
- Weak correlation treated as signal.
- Seasonal noise mistaken for subsurface change.
- Station metadata error changes interpretation.
- Instrument change or data gap creates false alert.
- Validation rule: stack stability, station metadata audit, seasonal flag, and human review before monitoring claims.

Website tasks:
- Add more NoisePy deck screenshots if available.
- Add stable versus unstable CCF visual.
- Add a parameter/provenance strip showing window length, filter, station pair, and stack count.

### 11. Can The Current Stock App Teach Honest AI App Building?

Current example:
- Current Streamlit stock app visuals: all-tickers chart, saved-data chart, Codex app pipeline, GitHub/Streamlit workflow.
- The topic should teach that building an AI app is different from making trustworthy predictions.

New use cases:
- Finance: honest dashboards that show baselines, leakage checks, and drift before any prediction language.
- Sales: forecast app with walk-forward validation and drift monitoring.
- Inventory: demand planning app where stale data and seasonality are visible.
- Marketing: campaign performance app that separates correlation from causal claims.

Visual to build:
- "Honest App Risk Pipeline" diagram. Saved data -> feature window -> train/evaluation date split -> baseline model -> challenger model -> walk-forward test -> Streamlit chart -> drift monitor -> claim language gate.
- Processing sketch: a shiny dashboard tries to pass through a red gate. It only passes if baseline, walk-forward, and drift checks are complete.

ML pipeline and architecture:
1. Load saved ticker data with refresh timestamp.
2. Create features using only past data available at each prediction point.
3. Split by date using walk-forward evaluation.
4. Compare naive baseline, simple model, and challenger model.
5. Track performance by market regime, ticker, and time window.
6. Add drift monitoring for feature distributions and error distributions.
7. Render Streamlit charts with cautious language and clear limits.

ML source implementation:
- Spatial CV source is not direct finance, but the same leakage principle applies: block by time, not random rows.
- GUI/ADEPT sources: app-building workflow, Codex changes, artifact handoff.
- DOE AI for Energy: human oversight and decision-support framing can generalize to finance/product apps.

Error and validation gates:
- Future data leakage.
- Overfit dashboard with no baseline.
- Stale refresh treated as current.
- Survivorship bias or ticker selection bias.
- Prediction language overclaims usefulness.
- Validation rule: walk-forward test, baseline comparison, refresh timestamp, drift report, and finance-language review.

Website tasks:
- Keep using current stock chart exports, not old diagrams.
- Add a drift monitor visual and leakage gate.
- Add a "dashboard claim checklist" before the output.

### 12. SEM Petrography, Thin Sections, And Proxy Claims

Current example:
- SEM/thin-section and rock classification visuals can become labeled examples, but climate or reservoir proxy claims need separate evidence.
- This topic should be about separating visible image labels from interpreted scientific claims.

New use cases:
- Materials QA: classify grain, fracture, pore, or defect textures from microscopy.
- Agriculture: classify soil microstructure or mineral indicators.
- Manufacturing: detect defects in surfaces or components.
- Energy/reservoir: label petrographic textures while keeping reservoir/proxy claims under expert review.

Visual to build:
- "Observation vs Interpretation" diagram. Image crop -> visible label proposal -> expert correction -> literature link -> proxy-claim gate -> accepted/rejected interpretation.
- Processing sketch: labels attach to visible grains, but unsupported proxy labels bounce off a red gate.

ML pipeline and architecture:
1. Ingest SEM images, thin-section photos, scale bars, sample metadata, and literature references.
2. Crop image fields and propose visible labels: grain texture, mineral label, pore/fracture, kaolinite form.
3. Separate observation labels from interpretation labels.
4. Use expert corrections to improve label examples.
5. Link proxy claims to literature and sample context before showing them.
6. Output reviewable label set and blocked unsupported claims.

ML source implementation:
- GUI/ADEPT sources for human correction and review queues.
- Spatial/GeoAI validation logic for sample/area splits when images come from related samples.
- Physics-informed ML principle: interpretations must obey domain constraints and source evidence.

Error and validation gates:
- Texture label overclaim.
- Proxy meaning inferred from image alone.
- Detrital/authigenic confusion.
- Missing scale or sample context.
- Validation rule: visible-label audit, expert petrography review, literature support, and ambiguous-example bucket.

Website tasks:
- Add a label/proxy split visual.
- Add examples from materials QA and manufacturing so non-geoscience viewers understand the workflow.
- Keep unsupported interpretations visibly blocked.

## Cross-Topic Architecture Patterns To Add

### Pattern A: Source-Backed AI/ML Architecture

Use for: every topic.

Flow:
Source images and files -> metadata/provenance -> feature extraction -> model or graph layer -> validation gate -> human review -> output.

Required error labels:
- missing source
- weak label
- leakage
- domain shift
- uncertain output

### Pattern B: Human-In-The-Loop Review

Use for: agent workflows, knowledge graphs, geophysics, hydrates, stock app, SEM.

Flow:
AI proposal -> confidence/uncertainty -> reviewer decision -> correction log -> updated training/evaluation set.

Required error labels:
- reviewer disagreement
- ambiguous instruction
- unsupported claim

### Pattern C: Leakage-Safe Evaluation

Use for: hydrates, stock app, satellite classification, earthquake windows, geophysical surveys.

Flow:
raw data -> split policy -> transform fit on training only -> model -> held-out validation -> calibration -> deployment gate.

Required error labels:
- random-row leakage
- future leakage
- spatial leakage
- target leakage

### Pattern D: Foundation Model With Task Head

Use for: seismic, ambient noise, possibly agent traces.

Flow:
large pretraining corpus -> pretrained representation -> task-specific head -> calibration -> human review.

Required error labels:
- domain mismatch
- weak fine-tuning labels
- overconfident transfer

## Prioritized Rollout

### Phase 1 - Make The ML Sources Visible

1. Add the ML source tracker in Build Room.
2. Move ML architecture panels higher on topic pages.
3. Add source-keyword chips under every ML diagram.
4. Add direct image panels for every embedded source link.

### Phase 2 - Build The Highest-Value Visuals

1. Hydrate leakage-safe architecture.
2. Agent trace factory.
3. Knowledge graph AI/ML hub.
4. Phone-to-cloud scientific run.
5. Satellite classifier with spatial CV.
6. Ambient noise monitoring ladder.

### Phase 3 - Add Processing Sketches

1. Action traces from screen recording.
2. GraphRAG edge growth.
3. 3D-to-2D feature conversion.
4. Cloud data run and GitHub commit.
5. Geophysical disagreement board.
6. Hydrate leakage gate.

### Phase 4 - Tighten Credibility

1. Every topic gets an error panel.
2. Every ML pipeline shows split policy.
3. Every prediction-like idea states what it does not claim.
4. Every source visual is local or rendered in-page, not only linked out.

## Completion Definition

A topic should not be considered complete until it has all of the following:

- visible real source image or screenshot
- one current example
- one cross-sector use case
- one visual concept to build
- one ML architecture or pipeline
- named ML-source vocabulary
- explicit error and validation gates
- no unsupported prediction claim
- no link-only evidence where an image is needed

