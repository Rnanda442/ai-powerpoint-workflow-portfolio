# Visual Instruction Manual - June 11, 2026

This document responds to the newest Gmail instruction, `AI powerpoint updates 6/11 new`, sent on June 11, 2026 at 5:11 PM Central.

Do not edit the website from this document alone. Use it as the visual-first execution manual for a later build pass.

## Core Instruction

The current site is too wordy. Each topic needs to teach the AI/ML concept with diagrams, lines, model components, icons, and motion ideas before adding more text.

For every topic, replace generic block/card explanations with a diagram that shows:

1. Real source evidence.
2. The current project example.
3. The future use case after an agent or model has the full evidence set.
4. The model or reasoning architecture.
5. Validation, leakage, uncertainty, or human-review gates.
6. A final output that is honest about what it supports.

## Visual Style From Reference Images

The newest email included reference images that point to two visual styles:

1. ML architecture diagram style
   - Use left-to-right or top-to-bottom flow.
   - Show inputs feeding encoders, feature boxes, model layers, validation gates, and outputs.
   - Use dashed boxes for sequences, repeated examples, or token arrays.
   - Use clear arrows and labels.
   - Example pattern: action sequence -> transformer/CNN encoders -> latent tokens -> decoder -> action sequence.

2. Teaching diagram style
   - Use simplified shapes to explain vocabulary.
   - For ensemble methods, show many small model units producing votes.
   - For every important vocabulary word, make a small visual if it helps learning.
   - Example pattern: instance -> tree 1/tree 2/tree n -> majority voting -> final class.

## Site-Wide Visual Rules

Use these rules before executing any topic redesign.

- Cut prose before adding art. If a paragraph explains a pipeline, convert it into a labeled diagram.
- Every important AI/ML vocabulary term should have a visual anchor: icon, lane, node, gate, token, tree, stack, or review marker.
- Do not use a single generic "ML pipeline" graphic for all topics. The model objective changes by topic.
- Show error and validation as visible parts of the architecture, not as footnotes.
- Use source-specific vocabulary from the two ML sources:
  - Hydrate paper: `Sgh`, NMR target, density, porosity, GR, Rt, Vp, Vs, caliper washout, GLOSS outliers, Keras/TensorFlow ANN, feature combinations, R2, cross-basin transfer.
  - CreditScore/ML notes: baseline first, correct split policy, Pipeline/ColumnTransformer, train-only transforms, shift-before-rolling, ETL checks, PSI/KS drift, segment monitoring, fallback model, rollback, fairness where people are affected.
- Add a "not allowed to claim" gate when the visual could be misread as a prediction or final scientific answer.
- For Processing or p5-style visuals, motion must explain the data transformation, not decorate the page.

## Visual Vocabulary Dictionary

Use these as small reusable teaching visuals across topics.

| Term | Draw It As | Why It Teaches |
| --- | --- | --- |
| UI token | A small labeled rectangle extracted from a screenshot, such as button, menu, layer name, or file path. | Shows that agents do not see "a website" vaguely; they need structured screen elements. |
| Action trace | A connected path of observe -> act -> inspect -> correct steps. | Turns screen recordings into supervised examples. |
| Rubric label | A green/red badge attached to an output or action segment. | Shows how human judgment becomes training/evaluation data. |
| Feature store | A shelf of named variables with source tags. | Shows that model inputs are organized and versioned. |
| Train-only transform | A lock around scaling/imputation fitted inside the training box only. | Makes leakage prevention visible. |
| Leakage gate | A red vertical barrier between target/future data and feature generation. | Teaches why fake performance happens. |
| Split policy | A fork labeled by time, well, region, sample, station, line, or task. | Shows that validation must match the real deployment situation. |
| Drift monitor | A gauge comparing baseline vs current distribution with PSI/KS labels. | Shows when a model input changed after deployment. |
| Abstention | A yellow "review" bin before output. | Shows that uncertain outputs should not be forced into final answers. |
| Human review | A person/checkpoint icon after model output and before publication. | Keeps expert judgment visible. |
| Source-backed edge | A solid graph edge with a citation tag. | Separates evidence from AI suggestion. |
| Inferred edge | A dashed graph edge with a review badge. | Shows that plausible relationships still need approval. |
| Stable CCF | A bright stacked waveform line. | Shows that ambient-noise monitoring requires repeatable signal. |
| Conflict zone | A striped or hatched area where methods disagree. | Prevents false visual consensus. |
| Proxy claim gate | A red/yellow gate between visible label and interpretation claim. | Prevents image labels from becoming unsupported climate or reservoir claims. |

## Global Page-Level Changes To Plan

### Homepage / Topic Wall

Build a thin route layer that connects source types to ML methods and validation gates:

- Screenshots/recordings -> action traces -> held-out task replay.
- Papers/slides/tables -> entity extraction -> source-backed graph.
- Maps/rasters -> spatial features -> spatial or region-held-out validation.
- Waveforms/noise -> station/pick features -> human-reviewed QA.
- Wells/logs -> `Sgh` feature table -> well-held-out validation.
- Apps/dashboards -> past-only features -> walk-forward validation and drift.

Visual instruction:
Use animated dots moving behind the topic wall. Each dot should pass through a small trust gate: provenance, leakage, uncertainty, drift, or human review.

### Topic Page Template

Every topic should follow this visible order:

1. Big question.
2. Current evidence strip.
3. Visual vocabulary mini-panel.
4. Main architecture diagram.
5. Failure gates.
6. Future use-case output.
7. Copy-light technical note.

Do not bury the architecture in expanders. The diagram should appear before long copy.

### Processing Visual Lab

Processing sketches should be treated as "visual ML thinking labs."

Each sketch needs five lanes:

1. Source.
2. Feature or token.
3. Model/reasoning.
4. Error gate.
5. Output.

## Topic 1 - How AI Agents Learn Scientific Software

Current topic:
Screenshots, software recordings, prompt/rubric work, QGIS/GIS tasks, and Codex-style file access.

Future use case:
An agent has prior recordings, prompt history, file trees, rubrics, and accepted outputs. It must execute a new scientific software task by itself, then stop for human review when risk is high.

Main visual:
`Trace Factory`

Diagram shape:

`prompt + rubric + recording + file tree -> UI tokens -> action trace encoder -> supervised label builder -> behavior-cloning transformer -> replay simulator -> held-out task score -> human approval`

What to draw:

- Left column: prompt page, task rubric, screen recording frame, file tree, final map/output.
- Extracted UI tokens: small boxes labeled layer, menu, button, filepath, CRS, parameter, output.
- Action sequence lane: observe state -> click/tool action -> inspect output -> correction.
- Model layer: CLIP/OCR state encoder plus behavior-cloning transformer.
- Replay lane: simulated QGIS/scientific software task.
- Output: accepted project output or human review queue.

Vocabulary visuals:

- UI token: screenshot elements converted into small token rectangles.
- Action trace: connected cursor path with time stamps.
- Rubric label: green pass/red fail label attached to output.
- Held-out task: a sealed test folder the model has not seen.

Failure gates:

- Hidden state missing from video.
- Shortcut memorization of screen layout.
- Ambiguous rubric.
- Unsafe file action.
- Failed replay on held-out task.

Processing sketch:
Animate random cursor/action dots. A path captures useful actions, rejects failed actions, and turns accepted actions into token boxes. End with an agent replay trail that must pass a rubric gate.

Copy-ready execution prompt:
Build a visual-first `Trace Factory` section for the AI workflow topic. Convert recordings, screenshots, prompts, rubrics, and file trees into UI tokens and action traces. Show CLIP/OCR state encoding, behavior-cloning transformer policy, replay simulator, held-out scientific software task validation, and human approval gates. Keep copy short and make UI tokens, action traces, rubric labels, and unsafe-action gates visible.

## Topic 2 - AI + Knowledge Graphs For Critical Minerals

Current topic:
REE thesis work, Mountain Pass/Bayan Obo, Gephi exports, graph nodes/edges, source-backed research synthesis.

Future use case:
An agent reads thesis sources, slides, tables, and diagrams, extracts candidate entities and relationships, then builds a queryable mineral-systems graph where every edge has evidence.

Main visual:
`Source-To-Graph AI Hub`

Diagram shape:

`papers + slides + CSV nodes + figures -> entity extraction -> ontology cleanup -> edge ranking -> GraphRAG retrieval -> human edge audit -> queryable graph`

What to draw:

- Left: source chunks from thesis PDF, slide text, captions, CSV node/edge tables, Adobe/Gephi graphics.
- Center: AI/ML hub with three outputs: knowledge graph, architecture diagram, scientific drawing.
- Entity lane: mineral, host rock, deposit, process, location, age, evidence source.
- Edge lane: observed, inferred, analog, conceptual, AI-suggested.
- Right: graph query examples and source-backed slide output.

Vocabulary visuals:

- Source-backed edge: solid edge with citation tag.
- Inferred edge: dashed edge with review badge.
- Ontology cleanup: duplicate nodes merging into one node.
- GraphRAG: question node retrieving source chunks through graph paths.

Failure gates:

- Hallucinated edge.
- Duplicate entity names.
- Unsupported relationship.
- Graph leakage.
- Visually strong edge with weak evidence.

Processing sketch:
Scattered entity dots orbit a prompt node, snap into mineral/host/fluid/process clusters, then grow edges. Solid edges pass; dashed AI-suggested edges pause at human review.

Copy-ready execution prompt:
Build a `Source-To-Graph AI Hub` diagram for the critical minerals topic. Use REE slides, Gephi exports, GraphML/CSV nodes, thesis figures, and source notes as inputs. Show SciBERT/MatSciBERT-style entity extraction, relation cross-encoder edge ranking, GraphRAG retrieval, observed/inferred/AI-suggested edge styling, and a human edge-audit gate. Make the graph teach source-backed reasoning, not generic research organization.

## Topic 3 - First AI Visualization: Earthquake Globe

Current topic:
Processing earthquake visualization and sonification from USGS event data.

Future use case:
The creative globe becomes a feature-engineering workbench. It converts spatial/time events into model-ready region-time rows, but does not claim forecasting unless evaluated.

Main visual:
`3D Visualization To Feature Table`

Diagram shape:

`USGS events -> globe/sound encoding -> flattening lens -> region-time feature rows -> Poisson/negative-binomial baseline -> LightGBM anomaly ranker -> chronological validation`

What to draw:

- Left: globe with latitude/longitude dots, depth color, magnitude size, event time.
- Middle: flattening lens that converts the visual into table rows.
- Right: feature table columns: region id, time window, count, magnitude bins, depth bins, cluster density, lagged history.
- Model path: simple count model first, flexible model second.
- Output: anomaly rank or event pattern view, not unsupported forecast.

Vocabulary visuals:

- Lagged feature: a window that only looks backward.
- Chronological split: train on older windows, test on newer windows.
- Visual overclaim gate: blocks "prediction" language if no target exists.

Failure gates:

- Look-ahead leakage.
- Duplicate/bad events.
- Rare-event imbalance.
- Spatial autocorrelation.
- Forecast claim without future-window test.

Processing sketch:
Event dots pulse on a globe, then slide into a horizontal timeline. Windows become rows. Future windows are locked away until the model is evaluated.

Copy-ready execution prompt:
Rebuild the earthquake globe topic as `3D Visualization To Feature Table`. Show USGS event variables becoming region-time feature rows through a flattening lens. Use Poisson or negative-binomial count models as reference, LightGBM only as a challenger, chronological validation, and a no-forecast-claim gate. The diagram should teach feature engineering from visualization.

## Topic 4 - Seismic Notebooks And Pondicherry

Current topic:
Pondicherry seismic notebooks, waveform download, station matching, arrival picking, velocity interpretation.

Future use case:
An agent turns exploratory notebooks into a waveform QA and arrival-pick review system.

Main visual:
`Seismic Notebook To QA Pipeline`

Diagram shape:

`catalog search -> station metadata -> waveform windows -> LightGBM QA -> PhaseNet/EQTransformer picks -> uncertainty band -> human-reviewed velocity table`

What to draw:

- Left: event catalog, station map, waveform file, notebook cell.
- QA lane: missing waveform, station mismatch, weak signal, SNR, channel check.
- Model lane: LightGBM waveform QA classifier, then PhaseNet/EQTransformer pick proposal.
- Uncertainty lane: pick-time band around P/S arrivals.
- Output: reviewed pick table, velocity estimate, caveat tag.

Vocabulary visuals:

- Waveform window: a trace segment with expected arrival zone.
- Pick proposal: vertical line plus probability band.
- Human-reviewed pick: accepted line with reviewer mark.

Failure gates:

- Station mismatch.
- Weak waveform.
- Bad metadata.
- Manual pick uncertainty.
- Interpretation before pick review.

Processing sketch:
Noisy traces scroll. A scanner proposes pick lines. Good picks turn green, weak picks stay yellow, rejected picks move into review.

Copy-ready execution prompt:
Build a `Seismic Notebook To QA Pipeline` diagram for Pondicherry. Use catalog search, station metadata, ObsPy waveform windows, SNR/metadata QA, LightGBM waveform quality classifier, PhaseNet/EQTransformer pick proposal, bootstrap or confidence-band uncertainty, and human-reviewed velocity output. Make uncertainty visible around the pick line.

## Topic 5 - AI For Energy Screening Workflows

Current topic:
North Slope public-source atlas, GIS layers, source library, structural explorer, hydrate/wireline ML planning.

Future use case:
An expert-reviewed hydrate screening architecture predicts or ranks gas hydrate intervals using logs and geologic context, while blocking leakage and overconfident public claims.

Main visual:
`Leakage-Safe Hydrate Architecture`

Diagram shape:

`public sources + wells + logs -> CRS/depth/QC gates -> caliper washout + GLOSS -> train-only normalization -> Keras ANN Sgh regressor -> XGBoost challenger -> leave-well/basin validation -> calibration/abstention -> geologic review`

What to draw:

- Source lane: maps, stratigraphy, source library, well IDs, formation tops.
- Log lane: density, density porosity, GR, Rt, Vp, Vs.
- Target lane: NMR-derived `Sgh`.
- QC lane: missing log row removal, caliper washout, GLOSS outliers, unit normalization.
- Red leakage barrier: prevents target labels or future information from leaking into feature engineering.
- Model lane: Ridge/ElasticNet reference, Keras/TensorFlow ANN, XGBoost/LightGBM challenger.
- Output lane: hydrate occurrence/saturation screen, calibrated confidence, abstain/review bin.

Vocabulary visuals:

- `Sgh`: target droplet/borehole interval derived from NMR.
- Caliper washout: widened borehole segment crossed out.
- GLOSS outlier: depth-point dot flagged in multi-feature space.
- Leave-well-out split: complete wells held out as sealed test wells.
- Abstention: uncertain interval routed to geologist review.

Failure gates:

- Target leakage.
- Random depth-row split.
- Missing high-value logs.
- Gas/ice/cement lookalikes.
- Poor calibration.
- Public map overclaim.

Processing sketch:
Papers, GIS layers, logs, and wells stack into a feature table. Bad rows fall through washout/GLOSS gates. A red leakage wall separates target labels from train-only feature transforms. Uncertain intervals move to a review bin.

Copy-ready execution prompt:
Build a large `Leakage-Safe Hydrate Architecture` diagram for North Slope. Use the hydrate paper vocabulary: five-well style dataset, NMR-derived `Sgh`, density, porosity, GR, Rt, Vp, Vs, caliper washout, GLOSS outlier detection, Keras/TensorFlow ANN, feature-combination testing, R2/MAE/RMSE, and cross-basin transfer. Add the stronger portfolio gate: leave-well-out or basin-held-out validation, calibration, abstention, and geologist review.

## Topic 6 - AI For Visual Geoscience Classification

Current topic:
Rock classification, petrography, geochemistry diagrams, thin-section decks, formation tables, graph outputs.

Future use case:
Images, chemistry, diagrams, and text labels become a multimodal training set with expert-reviewed labels.

Main visual:
`Multimodal Rock Label Pipeline`

Diagram shape:

`thin sections + classification charts + spider diagrams + formation tables -> label/metadata audit -> image branch + chemistry branch + text branch -> late-fusion label ranker -> expert correction queue`

What to draw:

- Image branch: thin-section or map crop -> EfficientNet/ResNet embedding.
- Chemistry branch: ratios, spider values, formation variables -> XGBoost/LightGBM.
- Text/source branch: caption/source label -> embedding or rule label.
- Fusion layer: combines branches only after metadata is visible.
- Output: ranked rock/mineral labels plus ambiguous bucket.

Vocabulary visuals:

- Sample-held-out split: all crops from one sample stay together.
- Weak label: label with warning icon.
- VIF/correlation check: chemistry variables connected by high-correlation lines.
- Expert audit: correction loop back to training examples.

Failure gates:

- Same-sample crop leakage.
- Missing scale/context.
- Mixed class definitions.
- Correlated chemistry misread as causation.
- Overconfident visual label.

Processing sketch:
Particles representing image, chemistry, and label evidence pass through separate filters, combine into class nodes, and uncertain classes route to expert review.

Copy-ready execution prompt:
Build a `Multimodal Rock Label Pipeline` diagram. Use thin-section images, chemical classification charts, spider diagrams, formation tables, and source captions. Show EfficientNet/ResNet image branch, XGBoost/LightGBM chemistry branch, text/source context branch, late-fusion label ranker, sample-held-out validation, weak-label warnings, VIF/correlation check, and expert correction queue.

## Topic 7 - SAGE / Valles Caldera Geophysics

Current topic:
Field geophysics, gravity maps, EM/TEM/ERT, seismic, field notes, Valles/SAGE evidence.

Future use case:
AI ranks agreement/conflict zones across imperfect methods without flattening uncertainty into one false answer.

Main visual:
`Geophysical Disagreement Board`

Diagram shape:

`gravity + EM/TEM + ERT + seismic + geology -> shared spatial frame -> method-specific features -> conflict classifier -> GP uncertainty surfaces -> expert disagreement board`

What to draw:

- Method lanes: gravity, EM/TEM, ERT, seismic, geology, field notes.
- Each lane has its own color, uncertainty ribbon, and acquisition/processing note.
- Agreement zones: glow where methods align.
- Conflict zones: striped/hatch marks where methods disagree.
- Model lane: LightGBM/random forest conflict ranker, Gaussian Process uncertainty surface.
- Output: review-priority board, not final subsurface truth.

Vocabulary visuals:

- Method physics: icon per instrument/method.
- Misregistration: shifted layers with red offset arrows.
- False consensus gate: blocks smoothed map if conflict zones are hidden.

Failure gates:

- Misregistration.
- Acquisition artifact.
- Method physics ignored.
- False consensus.
- Smooth map overclaim.

Processing sketch:
Translucent geophysical fields slide into alignment. Agreement glows, but conflicts remain striped and pinned for expert review.

Copy-ready execution prompt:
Build a `Geophysical Disagreement Board` for Valles/SAGE. Use method lanes for gravity, EM/TEM, ERT, seismic, geology, and field notes. Show shared spatial registration, method-specific uncertainty, LightGBM conflict ranking, Gaussian Process uncertainty surfaces, striped conflict zones, and expert review. Do not merge methods into one clean answer.

## Topic 8 - AI For Near-Surface Geophysics

Current topic:
Near-Surface Dwellers / fen investigation, hammer seismic, transient EM, ERT, geologic units, line intersections.

Future use case:
An agent compares shallow methods line-by-line and flags where methods agree, conflict, or need field review.

Main visual:
`Fen Method Fusion Cross-Section`

Diagram shape:

`hammer seismic + ERT + TEM + field notes -> line geometry -> velocity/resistivity/conductivity table -> agreement/conflict ranker -> leave-line-out validation -> review targets`

What to draw:

- Cross-section with separate layers:
  - hammer seismic velocity
  - ERT resistivity
  - TEM conductivity
  - possible unit labels
  - field notes
- Line intersections as vertical markers.
- Agreement zones glow.
- Conflict zones stay striped.
- Output is review target, not asserted geologic unit.

Vocabulary visuals:

- Line-aware validation: one survey line held out.
- Possible unit: label with question mark.
- Field-note context: small notebook icon attached to a zone.

Failure gates:

- Wrong line intersection.
- Field-note loss.
- Possible unit becoming asserted unit.
- Clean overlay overclaim.
- Leave-line-out failure.

Processing sketch:
Survey lines sweep across a fen cross-section. Method layers move into place. Intersections pulse. Conflicts hatch red/yellow and pause for review.

Copy-ready execution prompt:
Build a `Fen Method Fusion Cross-Section` diagram. Use hammer seismic velocity, ERT resistivity, TEM conductivity, possible units, field notes, and line intersections as separate lanes. Show LightGBM method-conflict ranking, Gaussian Process or method-specific uncertainty surfaces, leave-line-out validation, and review targets. Preserve disagreement visually.

## Topic 9 - Supervised ML For Moho Depth Mapping

Current topic:
Australia-to-USA gravity/Moho supervised ML project, ANN-style model, transfer question.

Future use case:
The model is evaluated for regional transfer, not just local score. Residual maps and failure zones are the main story.

Main visual:
`Regional Transfer Evaluation`

Diagram shape:

`Australia training region -> gravity/topography/crustal features -> Ridge/GAM reference -> LightGBM/XGBoost regressor -> ANN challenger -> USA transfer test -> residual map -> leakage/risk checklist`

What to draw:

- Left map: training region.
- Feature shelf: gravity anomaly, topography, crustal proxy, region id.
- Model ladder: simple baseline, tree/boosted model, ANN challenger.
- Transfer bridge: model leaves Australia and lands on USA region.
- Output: residual map with red/blue errors and uncertainty zones.

Vocabulary visuals:

- Spatial leakage: train/test cells too close with warning line.
- Transfer test: bridge between regions.
- Residual: prediction minus observed dot.
- Coordinate memorization: coordinate feature blocked or flagged.

Failure gates:

- Spatial leakage.
- Biased train/test boundary.
- Hidden variable mismatch.
- Coordinate memorization.
- High score without transfer.

Processing sketch:
Training points feed a neural-node chain. Predictions land on a new region. Residual dots flash where transfer fails.

Copy-ready execution prompt:
Build a `Regional Transfer Evaluation` diagram for Moho ML. Show Australia training data, gravity/topography/crustal features, Ridge/GAM reference, LightGBM/XGBoost regressor, ANN challenger, USA transfer test, residual/error map, leave-region-out validation, coordinate-memorization warning, and spatial leakage gate.

## Topic 10 - AI For Ambient-Noise Seismology

Current topic:
NoisePy, continuous records, station pairs, cross-correlation, stacking, monitoring.

Future use case:
AI triages which station-pair correlations are stable enough for monitoring and which are data gaps, instrument changes, seasonal noise, or weak correlations.

Main visual:
`Ambient Noise Monitoring Ladder`

Diagram shape:

`continuous station records -> windows -> preprocessing -> station-pair CCF -> stable stack -> change metric -> anomaly triage -> alert review`

What to draw:

- Station nodes connected by pair arcs.
- Trace windows flowing into preprocessing.
- CCF stack: weak lines fade, stable lines brighten.
- QA model: LightGBM CCF-quality classifier.
- Anomaly model: Isolation Forest or robust anomaly triage.
- Future layer: SeisLM-style embedding challenger.
- Output: alert review queue with provenance.

Vocabulary visuals:

- Stable CCF: repeated waveforms stacking brighter.
- Stack count: numeric badge on a station-pair line.
- Seasonal flag: calendar icon.
- Freshness check: max loaded timestamp gauge.

Failure gates:

- Weak correlation treated as signal.
- Seasonal noise mistaken for subsurface change.
- Station metadata error.
- Data gap.
- Instrument change.

Processing sketch:
Noise traces from many stations flow into pair arcs. Stable pairs brighten into a central stack. Unstable pairs flicker and fall into QC.

Copy-ready execution prompt:
Build an `Ambient Noise Monitoring Ladder` diagram. Use continuous records, station metadata, windows, preprocessing, station-pair CCF, stable stack, change metric, LightGBM stability classifier, Isolation Forest anomaly triage, SeisLM-style future embedding layer, freshness checks, seasonal flags, and human alert review.

## Topic 11 - AI App Building, Automation, And Model Risk

Current topic:
Stock dashboard, Codex-built Streamlit app, GitHub/pipeline workflow, model-risk discussion.

Future use case:
The app teaches honest AI app building: baselines, past-only features, walk-forward testing, drift monitoring, and cautious claim language.

Main visual:
`App Risk And Leakage Gate`

Diagram shape:

`saved ticker data + refresh time -> past-only feature windows -> chronological split -> persistence/moving-average baseline -> ElasticNet/LightGBM challenger -> walk-forward validation -> PSI drift monitor -> claim-language gate`

What to draw:

- Input: saved ticker database and refresh timestamp.
- Feature window: past-only rolling features with `shift(1)` shown visibly.
- Split: train past, validate future.
- Model ladder: persistence baseline, ElasticNet, LightGBM.
- Monitoring: PSI/KS, missingness, stale data, segment/ticker performance.
- Output: dashboard with claim gate: demo/research tool, not investment advice.

Vocabulary visuals:

- Shift-before-rolling: current row blocked from seeing itself.
- Walk-forward validation: sliding train/test windows.
- Drift gauge: baseline vs current PSI.
- Fallback model: alternate path when drift or stale data fails.

Failure gates:

- Future leakage.
- No baseline.
- Stale refresh.
- Ticker universe bias.
- Drift hidden by overall score.
- Overclaiming prediction usefulness.

Processing sketch:
File dots fall into a Codex node, sort into GitHub branches and dashboard panels, then pass through a leakage/drift gate before any claim appears.

Copy-ready execution prompt:
Build an `App Risk And Leakage Gate` diagram around the stock dashboard topic. Show saved ticker data, refresh timestamp, past-only features with shift-before-rolling, chronological/walk-forward split, persistence and moving-average baselines, ElasticNet/LightGBM challenger, PSI/KS drift monitor, stale-data flag, fallback path, and claim-language gate.

## Topic 12 - AI For SEM Petrography And Climate Proxies

Current topic:
SEM petrography, clay minerals, morphology labels, detrital/authigenic interpretation, paleoclimate or reservoir proxy claims.

Future use case:
AI proposes visible petrographic labels while proxy interpretations remain blocked until expert and literature evidence supports them.

Main visual:
`Observation Vs Interpretation Gate`

Diagram shape:

`SEM crop + scale + sample metadata -> visible label proposal -> expert correction -> literature link -> proxy claim gate -> accepted observation or blocked interpretation`

What to draw:

- Left: SEM image crop with scale bar and sample ID.
- Label layer: grain, pore/fracture, clay morphology, mineral texture, ambiguous.
- Model lane: EfficientNet/ResNet patch classifier, optional U-Net/Mask R-CNN segmentation, CLIP retrieval of similar reviewed examples.
- Interpretation lane: detrital/authigenic, paleoclimate proxy, reservoir claim.
- Proxy claim gate: blocks unsupported interpretations.

Vocabulary visuals:

- Visible label: label tied to observable texture.
- Interpretation label: label requiring evidence beyond image pixels.
- Literature support: citation card connected to claim.
- Ambiguous bucket: examples saved for expert review.

Failure gates:

- Texture overclaim.
- Missing scale.
- Detrital/authigenic confusion.
- Proxy claim from image alone.
- Literature mismatch.

Processing sketch:
SEM-like grayscale texture moves under a magnifier. Labels snap to grains. Unsupported proxy labels bounce off a red gate until source/expert support appears.

Copy-ready execution prompt:
Build an `Observation Vs Interpretation Gate` diagram for SEM petrography. Use SEM crops, scale bars, sample metadata, visible label proposals, EfficientNet/ResNet patch classification, U-Net/Mask R-CNN segmentation if masks exist, CLIP retrieval of similar expert-labeled examples, expert correction, literature support, and a proxy-claim gate that blocks unsupported paleoclimate or reservoir interpretation.

## Research And Visualization Work Before Execution

Before implementing any visual, collect the exact source evidence for that topic:

| Topic | Must Find First |
| --- | --- |
| AI agents | Best screenshots/recordings, rubric examples, file tree examples, final output examples. |
| Knowledge graph | GraphML/CSV node-edge exports, REE slide sequence, thesis figure/caption examples. |
| Earthquake globe | Correct 54-second LinkedIn video or poster frame, USGS event schema, Processing sketch evidence. |
| Pondicherry | Notebook cells, station map, waveform image, annotated pick/velocity panel. |
| North Slope | Well/log variable panel, map, source-library entry, hydrate paper figure/table concepts. |
| Rock classification | Thin-section deck image, chemical classification chart, spider diagram, formation label table. |
| Valles | Bouguer/free-air/Moho maps, SAGE deck image, method-specific uncertainty notes. |
| Near surface | Near-Surface Dwellers deck panels, line intersection image, method panels. |
| Moho ML | Notebook/report variables, training/test geography, output/residual image. |
| Ambient noise | NoisePy station-pair/CCF/stack screenshot, processing parameter examples. |
| Stock workflow | Current dashboard screenshots, data refresh/pipeline evidence, model baseline notes. |
| SEM petrography | SEM deck images, scale/sample context, label examples, proxy interpretation notes. |

## Execution Priority

1. North Slope `Leakage-Safe Hydrate Architecture`
   - Most source-backed and highest technical payoff.
2. AI agent `Trace Factory`
   - Best match to the future-agent instruction.
3. Knowledge graph `Source-To-Graph AI Hub`
   - Best topic for concept graph and architecture visuals.
4. Stock `App Risk And Leakage Gate`
   - Best use of CreditScore/ML reliability source.
5. Pondicherry `Seismic Notebook To QA Pipeline`
   - Strong notebook-to-ML pipeline story.
6. Ambient noise `Monitoring Ladder`
   - Strong continuous-data pipeline story.

## Completion Checklist For Each Topic

A topic visual is complete only when it has:

- One real source image or asset.
- One vocabulary mini-visual.
- One architecture diagram.
- One explicit model or reasoning layer.
- One split/validation policy.
- One failure gate.
- One human-review checkpoint.
- One honest output.
- Less prose than the current page section.
- No unsupported prediction or proxy claim.

## Next Build Pass Prompt

Use this prompt in a new execution chat when ready:

Read `docs/VISUAL_INSTRUCTION_MANUAL_2026-06-11.md`, `docs/ML_MODEL_DETAIL_SPEC_2026-06-11.md`, and `data/ml_diagram_tracker.csv`. Do not add generic ML pipeline blocks. For each topic, implement the named visual architecture in the site order, using source-specific vocabulary and real assets. Start with the North Slope hydrate architecture, then the AI agent trace factory, then the knowledge graph hub. Keep prose short, make vocabulary visual, and show validation/error gates directly inside the diagrams.
