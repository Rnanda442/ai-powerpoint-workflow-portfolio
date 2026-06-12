# ML Topic Transfer Patterns - June 12, 2026

Use this as the next-pass framing rule for the Think Tank Topics page:

**Vague topic -> concrete example project -> reusable ML pattern for other sectors.**

The site should not only say "this project is about North Slope" or "this project is about thesis graphs." It should show the example project, the ML/AI structure underneath it, and how that same structure transfers to other industries.

## 1. AI Workflow / Trace Factory

Example: QGIS/Vagon/software recordings becoming agent training data.

Reusable pattern: any technical workflow can become supervised action traces.

`prompt/rubric + screen recording + file tree -> UI tokens -> action trace -> CLIP/OCR state encoder -> behavior-cloning transformer -> replay simulator -> held-out task score -> unsafe action gate -> human review`

## 2. Thesis Graph / Source-To-Graph AI Hub

Example: REE thesis, Gephi, GraphML, slides, source notes.

Reusable pattern: source-backed graph reasoning for any research-heavy field.

`papers + slides + CSV nodes + figures -> entity extraction -> ontology cleanup -> relation cross-encoder -> source-backed/inferred edges -> GraphRAG retrieval -> GraphSAGE/R-GCN -> human edge audit -> queryable graph`

## 3. Earthquake Globe / Visualization To Feature Table

Example: USGS earthquake globe and sonification.

Reusable pattern: visual data exploration becomes model-ready rows.

`USGS events -> globe/sound encoding -> flattening lens -> region-time feature rows -> lagged features -> Poisson/negative-binomial baseline -> LightGBM anomaly ranker -> chronological validation -> no-forecast claim gate`

## 4. Seismic / Notebook To QA Pipeline

Example: Pondicherry waveform notebooks and velocity analysis.

Reusable pattern: exploratory notebooks become QA and review systems.

`catalog search -> station metadata -> waveform windows -> SNR/metadata QA -> LightGBM waveform QA -> PhaseNet/EQTransformer picks -> uncertainty band -> human-reviewed velocity table`

## 5. North Slope / Leakage-Safe Hydrate Architecture

Example: public sources, logs, hydrate screening, structural explorer.

Reusable pattern: public/domain data becomes expert-reviewed screening architecture.

`public sources + wells + logs -> CRS/depth QC -> caliper washout + GLOSS -> leakage barrier -> train-only normalization -> Keras ANN Sgh regressor -> XGBoost challenger -> leave-well-out validation -> calibration/abstention -> geologist review`

## 6. Rock Classification / Multimodal Rock Label Pipeline

Example: thin sections, geochemistry charts, spider diagrams, formation tables.

Reusable pattern: image + tabular + text evidence becomes reviewed labels.

`thin sections + charts + chemistry + formation tables -> label/metadata audit -> image branch -> chemistry branch -> text/source branch -> late-fusion label ranker -> sample-held-out validation -> expert correction queue`

## 7. Valles / Geophysical Disagreement Board

Example: gravity, EM/TEM, ERT, seismic, field notes.

Reusable pattern: imperfect methods are compared without forcing false agreement.

`gravity + EM/TEM + ERT + seismic + geology -> shared spatial frame -> method-specific features -> conflict zones -> LightGBM conflict ranker -> Gaussian Process uncertainty -> expert disagreement board`

## 8. Near Surface / Fen Method Fusion Cross-Section

Example: hammer seismic, ERT, TEM, line intersections, field notes.

Reusable pattern: field methods become review targets, not over-clean maps.

`hammer seismic + ERT + TEM + field notes -> line geometry -> velocity/resistivity/conductivity lanes -> conflict ranker -> leave-line-out validation -> review target`

## 9. Moho ML / Regional Transfer Evaluation

Example: Australia-to-USA gravity/Moho transfer question.

Reusable pattern: model credibility depends on geographic transfer, not local score.

`Australia training data -> gravity/topography/crustal features -> Ridge/GAM reference -> LightGBM/XGBoost regressor -> ANN challenger -> USA transfer test -> residual map -> spatial leakage/coordinate memorization gate`

## 10. Ambient Noise / Monitoring Ladder

Example: station-pair CCFs, stacks, NoisePy-style monitoring.

Reusable pattern: continuous signals become stable/unstable monitoring products.

`continuous records -> station windows -> preprocessing -> station-pair CCF -> stable stack -> LightGBM CCF-quality classifier -> Isolation Forest anomaly triage -> freshness/seasonal gates -> human alert review`

## 11. Stock Workflow / App Risk And Leakage Gate

Example: Streamlit stock dashboard and model-risk framing.

Reusable pattern: dashboard predictions need leakage, drift, and claim controls.

`saved ticker data + refresh time -> shift-before-rolling features -> chronological split -> persistence/moving-average baseline -> ElasticNet/LightGBM challenger -> walk-forward validation -> PSI/KS drift monitor -> fallback path -> claim-language gate`

## 12. SEM Petrography / Observation Vs Interpretation Gate

Example: SEM crops, clay morphology, proxy interpretation risk.

Reusable pattern: AI can label observations, but claims need evidence gates.

`SEM crop + scale bar + sample metadata -> visible label proposal -> EfficientNet/ResNet patch classifier -> U-Net/Mask R-CNN or CLIP retrieval -> expert correction -> literature link -> proxy claim gate -> accepted observation or blocked interpretation`

## Next Site Pass Rule

Each topic should explicitly say:

**"This example teaches this reusable ML architecture."**
