# ML Diagram Outline And Tracking Plan - June 11, 2026

This is the working outline for turning every topic/project into a detailed ML diagram or ML pipeline panel. The goal is to make the site show how real evidence becomes model-ready structure, where validation happens, and what should be tracked before any claim becomes credible.

## Sources Found

The two actual ML sources from the June 11, 2026 self-sent email `ML sources` are:

1. `s10596-022-10151-9.pdf`
   - Paper: `Application of machine learning to characterize gas hydrate reservoirs in Mackenzie Delta (Canada) and on the Alaska north slope (USA)`.
   - Use for: North Slope, gas hydrate screening, well-log ML architecture, geoscience transfer testing, feature-combination diagrams, outlier/QC gates, and reservoir-parameter prediction.
2. `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`
   - Notes: predictive modeling, validation schemes, leakage-safe pipelines, rolling features, ETL quality checks, drift triage, KPI dashboards, and a CreditScoreV4 production incident.
   - Use for: every topic's validation layer, especially baseline-vs-flexible-model logic, train/test split design, leakage prevention, data quality monitoring, drift/PSI checks, segment/fairness monitoring, fallback models, and incident response.

Earlier Gmail intake also referenced `Codex_Website_Brand_Design_Workflow.docx`, but that is a site/workflow design source, not one of the two technical ML sources for the diagrams.

The repo-side planning sources that already translate prior source material into implementation language are:

1. `docs/ML_TOPIC_IMPROVEMENT_PLAN_2026-06-11.md`
2. `data/ml_future_roadmap.csv`

The main visual/evidence inventories to connect to the diagrams are:

- `data/project_visuals.csv`
- `data/source_inventory.csv`
- `data/case_studies.csv`
- `data/notebook_inventory.csv`
- `assets/topic_visuals/`
- `assets/project_visuals/`

## Diagram Standard

Each topic gets one source-backed ML architecture diagram using the same lane structure:

`source evidence -> cleaning/QC -> feature or representation layer -> model/reasoning layer -> validation gate -> human review -> output/decision`

Each diagram should show two separate objectives:

1. **Domain ML objective:** what the model or AI system is trying to predict, rank, extract, classify, or monitor.
2. **Reliability objective:** how the workflow prevents fake performance, leakage, stale data, drift, unsupported claims, or unreviewed output.

Every diagram should explicitly track:

- source asset or screenshot used as proof
- input data type and schema
- feature variables or extracted representations
- model family or reasoning layer
- split policy or evaluation design
- leakage and uncertainty risks
- human review checkpoint
- output or decision supported
- current status and next action

## Technical ML Vocabulary To Reuse

Use these two source vocabularies as the main anchors inside the diagrams.

### Source 1: Gas Hydrate Well-Log ML Paper

Use this vocabulary where the topic is about energy, geoscience, physical variables, well logs, transfer, or reservoir screening:

- ANN model trained in Keras/TensorFlow
- target variable: NMR-derived gas hydrate saturation, `Sgh`
- input logs: bulk density, density porosity, gamma radiation, resistivity, compressional velocity, shear velocity where available
- well-level dataset: Mount Elbert, Ignik Sikumi, Hydrate-01 / Kuparuk 7-11-12, Mallik 2L-38, Mallik 5L-38
- more than 10,000 depth points across five wells
- data preprocessing, hyperparameter tuning, well-log combination optimization, model validation
- caliper washout screening
- GLOSS outlier detection
- missing log row removal at corresponding depth points
- feature normalization
- two-log and three-log combination testing
- R2 / accuracy-style score for Sgh prediction
- basin transfer: train on one basin and test/predict in another basin

Important implementation note:
- The paper uses randomization and k-fold/80-20 validation language. For the portfolio diagrams, show this as a published reference point, but make the stronger website gate **well-held-out, area-held-out, or basin-held-out validation** when the claim is about transfer or deployment.

### Source 2: ML Project Reference And CreditScoreV4 Notes

Use this vocabulary on every topic's reliability layer:

- simple baseline before flexible models
- linear model, gradient boosting, KNN, neural network
- IID split versus chronological split
- rolling or walk-forward validation
- metrics by task: RMSE, MAE, R2, accuracy, ROC-AUC, PR-AUC, F1, calibration
- risk-model monitoring: score buckets, approval/decline rates, default-rate capture, segment performance
- multicollinearity and VIF
- leakage-safe preprocessing with Pipeline / ColumnTransformer
- fit transforms only on training data
- shift before rolling features
- duplicate timestamp tie-breakers
- ETL quality dimensions: completeness, uniqueness, validity, consistency, timeliness/freshness, reasonableness, reconciliation
- late-arriving data, watermarks, closed periods, aggregate versioning
- distribution-shift triage: sampling noise, pipeline issue, real business/domain change
- PSI/KS and feature-level drift
- segment-level monitoring
- fallback model or rollback path
- fairness metrics where people are affected: demographic parity, equal opportunity, equalized odds, calibration within groups, disparate impact ratio, predictive parity

The older broader ML source families below remain useful as future research vocabulary, but the two email sources above are the required basis for the next diagram pass:

- GUI agents survey: action trace, state observation, GUI grounding, trajectory supervision, held-out software task
- ADEPT scientific workflow agents: task graph, artifact handoff, runtime provenance, human checkpoint
- Geoscience knowledge graph pipeline: entity extraction, ontology, source-backed edge, schema audit
- Critical minerals GraphRAG: source chunk, graph query, ranked relationship, human edge review
- GNN mineral prospectivity mapping: node features, spatial edge, message passing, prospectivity score
- Spatial cross-validation for GeoAI: spatial block split, leave-area-out validation, spatial autocorrelation, domain shift
- SeisLM and seismic foundation models: pretrained waveform representation, task head, phase-pick uncertainty, station metadata
- Promptable seismic geobody model: promptable segmentation, geobody mask, interactive correction
- Physics-informed ML for subsurface energy: physics constraint, well-log feature transform, uncertainty calibration
- Gas hydrate well-log ML: hydrate occurrence head, saturation regression head, well-held-out split, calibration, abstention
- DOE AI for Energy report: energy decision support, human oversight, data governance
- USGS Earth MRI: public geoscience layer, mineral systems, source provenance, survey coverage

## Topic And Project Diagram Outlines

### 1. AI Workflow / Scientific Software Agents

Project key: `arcgis_raster_ml`

Diagram: Trace Factory.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is not reservoir prediction. The ML objective is to learn reliable task execution from software-use traces and evaluate it on held-out workflows.
- Use the case-notes source to make validation visible: held-out tasks, data quality checks, drift in task types, and fallback to human review.

How to make it:
- Start with screenshots, Vagon recordings, prompts, rubrics, file trees, and final outputs.
- Draw a step-by-step action trace lane: observe state, choose tool action, execute, inspect output, correct failure.
- Add a supervised example builder that attaches rubric labels and human corrections.
- End with an agent replay/evaluation box for held-out QGIS or scientific software tasks.

Track:
- action trace completeness
- prompt and rubric id
- tool used
- source file path
- pass/fail label
- correction reason
- unsafe action flag
- replay success on held-out task

Validation gates:
- hidden state missing
- shortcut memorization
- rubric ambiguity
- unsafe file action
- held-out task replay

### 2. Thesis Knowledge Graph / Critical Minerals

Project key: `thesis_knowledge_graph`

Diagram: Source-To-Graph AI Hub.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is not numeric prediction. The ML objective is relationship extraction, edge ranking, and graph-backed retrieval.
- Use the case-notes source to track data quality, schema validity, duplicate entities, drift in source coverage, and reviewer-approved edges.

How to make it:
- Use REE slides, Gephi exports, Excel node/edge tables, thesis figures, and source notes as inputs.
- Draw extraction of minerals, host rocks, locations, paragenesis, evidence sources, and deposit processes.
- Split graph edges into observed, inferred, conceptual, and AI-suggested.
- Add GraphRAG retrieval and a human edge-review gate before graph ML or prospectivity scoring.

Track:
- entity type
- synonym normalization
- edge type
- source-backed evidence
- confidence rank
- reviewer status
- graph query supported
- inferred edge warning

Validation gates:
- edge hallucination
- duplicate entity labels
- unsupported relationship
- graph leakage
- human edge audit

### 3. Processing Earthquake Globe

Project key: `processing_visuals`

Diagram: 3D Visualization To Feature Table.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is not a forecast unless an evaluated target is defined. The ML objective is feature transformation: spatial/time events become model-ready windows.
- Use the case-notes source for chronological splits, shift-before-rolling logic, baseline models, and warning gates against visual overclaiming.

How to make it:
- Start with USGS event variables: latitude, longitude, depth, magnitude, and event time.
- Show the 3D globe and sonification as the current visual layer.
- Add a flattening lens that converts events into time-window and region-window feature rows.
- End with baseline clustering or anomaly-tagging outputs plus a warning that visualization is not a forecast by itself.

Track:
- event source and pull date
- coordinate cleanup
- time-window definition
- magnitude/depth bin features
- cluster density
- lagged history
- train/test time boundary
- visual overclaim warning

Validation gates:
- look-ahead leakage
- duplicate or bad events
- rare-event imbalance
- spatial autocorrelation
- no prediction claim without evaluation

### 4. Pondicherry Seismic Notebooks

Project key: `pondicherry`

Diagram: Seismic Notebook To QA Pipeline.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.
Secondary analogy: `s10596-022-10151-9.pdf` for geoscience supervised targets and transfer discipline.

ML objective difference:
- This is waveform/event QA, not gas hydrate saturation. The target could be arrival-pick quality, event/station match validity, or velocity-estimate uncertainty.
- Use the case-notes source for train/test split, data quality, missingness, and model monitoring. Use the hydrate paper as a geoscience example of clearly defining inputs, target, QC, and validation.

How to make it:
- Start with catalog search, station metadata, waveform download, notebooks, and annotated seismic panels.
- Draw waveform preprocessing, station matching, arrival-pick proposal, manual review, velocity calculation, and uncertainty output.
- Add optional future ML task heads for event triage, arrival picking, and waveform QA.

Track:
- event id
- station id
- channel
- waveform availability
- pick time
- pick uncertainty
- SNR or QA flag
- reviewer decision
- velocity output provenance

Validation gates:
- station mismatch
- weak waveform signal
- manual pick uncertainty
- bad event metadata
- human-reviewed pick before interpretation

### 5. North Slope Energy Screening

Project key: `north_slope`

Diagram: Leakage-Safe Hydrate Architecture.

Primary ML source: `s10596-022-10151-9.pdf`.
Reliability source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is the topic closest to the paper. The ML objective is to predict or screen gas hydrate saturation/occurrence from available well logs and geologic context.
- The website version should improve the validation story by making leakage barriers, well-held-out validation, calibration, and abstention more explicit than a generic random split.

How to make it:
- Start with public geology layers, well context, stratigraphy, source-library entries, and wireline variables.
- Draw QC gates for CRS, depth alignment, missing logs, bad hole intervals, unit normalization, and formation tags.
- Put a visible red leakage barrier between target labels and feature transforms.
- Add the paper's saturation-regression target: NMR-derived `Sgh`.
- Optionally add a practical occurrence-classification head for public-facing screening.
- End with calibration, abstention, geologic review, and public-safe output.

Track:
- source provenance
- CRS and scale
- well id
- curve availability
- formation top
- feature transform version
- split policy
- occurrence metric
- saturation metric
- calibration and abstention status

Validation gates:
- target leakage
- random depth-row split
- missing high-value logs
- gas/ice/cement lookalike
- complete-well or area-held-out validation

### 6. Rock Classification And Geochemistry

Project key: `rock_classification`

Diagram: Multimodal Rock Label Pipeline.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.
Secondary analogy: `s10596-022-10151-9.pdf` for feature-combination testing and outlier/QC discipline.

ML objective difference:
- This is classification or label-ranking from images, diagrams, and chemistry, not well-log Sgh regression.
- Use the case-notes source to force baseline comparison, label quality checks, VIF/correlation review for tabular chemistry, and leakage-safe train/test splits by sample/site.

How to make it:
- Start with thin-section images, chemical classification charts, spider diagrams, formation rasters, and labels.
- Draw separate lanes for image features, geochemical/tabular features, and text/source context.
- Merge them only after metadata and label definitions are visible.
- End with ranked rock/mineral labels plus expert error review.

Track:
- image asset
- sample or formation id
- label source
- scale or context availability
- chemical variables
- diagram type
- model modality
- expert correction
- ambiguous-example bucket

Validation gates:
- weak labels
- missing sample context
- mixed class definitions
- overconfident visual label
- expert label audit

### 7. Valles / SAGE Geophysics

Project key: `valles_caldera`

Diagram: Geophysical Disagreement Board.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.
Secondary analogy: `s10596-022-10151-9.pdf` for physical variable QC and transfer testing across geologic settings.

ML objective difference:
- This is not one clean prediction. The ML objective is to rank agreement/conflict zones and review priority across imperfect survey methods.
- Use the case-notes source for data quality dimensions, drift/shift triage, and dashboard design that separates noise, data issue, and real field signal.

How to make it:
- Use gravity, EM/TEM/ERT, seismic, field notes, geology maps, and SAGE slide outputs as method lanes.
- Register all methods to a shared spatial frame.
- Show agreement zones as aligned signals and conflict zones as striped review zones.
- Use ML only to rank review priority unless labels and physics support a stronger model.

Track:
- method type
- survey geometry
- acquisition settings
- processing assumption
- spatial registration status
- method-specific uncertainty
- agreement/conflict label
- review priority

Validation gates:
- misregistration
- acquisition artifact
- method physics ignored
- false consensus
- expert review of conflict zones

### 8. Near-Surface Geophysics

Project key: `near_surface_geophysics`

Diagram: Fen Method Fusion Cross-Section.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is shallow-method comparison, not reservoir parameter prediction. The ML objective is to identify where methods agree, conflict, or need human review.
- Use the case-notes source for validation design, completeness checks, consistency checks, and line-aware held-out testing.

How to make it:
- Build a shallow cross-section with hammer seismic velocity, ERT resistivity, TEM conductivity, field notes, possible units, and line intersections.
- Keep each method as a separate lane instead of merging into one clean map.
- Highlight agreement points and mark conflicts as review targets.

Track:
- line id
- method id
- intersection location
- velocity/resistivity/conductivity values
- possible unit
- field-note context
- conflict status
- reviewer decision

Validation gates:
- wrong line intersection
- field-note loss
- unit label drift
- clean overlay overclaim
- leave-line-out or line-aware validation

### 9. Moho ML Transfer

Project key: `moho_ml`

Diagram: Regional Transfer Evaluation.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.
Secondary analogy: `s10596-022-10151-9.pdf` for cross-basin geoscience transfer.

ML objective difference:
- This is supervised geophysical regression/transfer, but the target is Moho depth instead of `Sgh`.
- Use the hydrate paper's basin-transfer framing, then use the case-notes source to require baseline comparison, leakage-safe preprocessing, residual review, and area-held-out validation.

How to make it:
- Start with Australian gravity/Moho training data and U.S. transfer target data.
- Draw feature preparation, model-family comparison, spatial split, residual maps, and transfer score.
- Make residual/error visualization the main output rather than a single accuracy score.

Track:
- variable list
- region id
- train/test geography
- model family
- baseline score
- challenger score
- residual map
- leakage check
- transfer failure zone

Validation gates:
- spatial leakage
- biased train/test boundary
- hidden variable mismatch
- high score without transfer
- leave-region-out validation

### 10. Ambient-Noise Seismology

Project key: `ambient_noise`

Diagram: Ambient Noise Monitoring Ladder.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is monitoring and anomaly triage, not static prediction. The ML objective is to separate stable station-pair signal from weak correlation, seasonal change, instrument change, or data gap.
- Use the case-notes source for timeliness/freshness, distribution shift, late data, monitoring thresholds, and incident-style alert response.

How to make it:
- Start with continuous records and station metadata.
- Draw windowing, preprocessing, station-pair CCF computation, stack stability, change metric, alert triage, and human review.
- Add foundation-model or representation-learning vocabulary only as a future layer after QA is clear.

Track:
- station pair
- window length
- filter parameters
- stack count
- CCF stability
- seasonal flag
- instrument change flag
- anomaly score
- alert review decision

Validation gates:
- weak correlation
- seasonal noise mistaken for signal
- station metadata error
- data gap or instrument change
- stable stack before monitoring claim

### 11. Stock Workflow / Honest App Building

Project key: `stock_dashboard`

Diagram: App Risk And Leakage Gate.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is the closest non-geoscience match to the case notes. The ML objective is honest time-based prediction/evaluation and production-style dashboard monitoring.
- Use the CreditScoreV4 incident as the model-risk analogy: feature drift, stale model assumptions, lagging outcomes, missing monitoring, fallback model, and careful claim language.

How to make it:
- Start with saved ticker data, refresh timestamp, notebook outputs, GitHub pipeline, and Streamlit charts.
- Draw feature windows, time-based split, naive baseline, challenger model, walk-forward test, drift monitor, and claim-language gate.
- Emphasize that the diagram is about honest app building, not investment advice.

Track:
- data refresh time
- ticker universe
- feature window
- prediction horizon
- baseline score
- challenger score
- walk-forward result
- drift metric
- stale-data flag
- claim language status

Validation gates:
- future leakage
- stale data
- no baseline
- survivorship or ticker bias
- walk-forward evaluation before prediction language

### 12. SEM Petrography

Project key: `sem_petrography`

Diagram: Observation Vs Interpretation Gate.

Primary ML source: `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`.

ML objective difference:
- This is label proposal and claim review, not direct climate/proxy prediction from an image.
- Use the case-notes source for label completeness, validity, segment/sample split, reviewer correction, and blocked unsupported claims.

How to make it:
- Start with SEM images, thin-section crops, sample metadata, scale bars, and literature references.
- Draw visible-label proposals first: grain texture, mineral label, pore/fracture, kaolinite form.
- Put a separate proxy-claim gate before paleoclimate or reservoir interpretation.
- End with accepted observations, blocked unsupported claims, and expert corrections.

Track:
- image crop
- scale bar
- sample context
- visible label
- interpretation label
- literature support
- expert correction
- ambiguity flag
- proxy claim status

Validation gates:
- texture label overclaim
- detrital/authigenic confusion
- missing scale
- proxy claim from image alone
- literature and expert review required

## Rollout Order

1. Build the CSV tracker and surface it in the Build Room.
2. Create the first six high-value diagrams: North Slope hydrate, agent trace factory, knowledge graph hub, rock classifier, Pondicherry seismic QA, stock risk gate.
3. Add the remaining diagrams for Valles, near-surface, Moho transfer, ambient noise, Processing earthquake features, and SEM interpretation.
4. Add source chips and validation gates to every topic page.
5. Only then add motion/Processing sketches so the motion reinforces the pipeline rather than replacing technical detail.

## Completion Definition

A topic diagram is complete only when it has:

- visible real source evidence
- an input/schema lane
- feature or representation lane
- model or reasoning lane
- validation gate
- human review checkpoint
- tracked metrics or review fields
- one explicit failure mode
- one output or decision
- no unsupported prediction claim
