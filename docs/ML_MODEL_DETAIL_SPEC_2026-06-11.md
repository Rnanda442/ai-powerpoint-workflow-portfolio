# ML Model Detail Spec - June 11, 2026

This document answers the June 11 instruction that the website plans need model details, not vague phrases like "baseline model" or "ML pipeline." Each topic should name the model class, target, inputs, labels, validation split, metrics, failure modes, and where human review happens.

Do not describe a topic as:

- "baseline model"
- "AI model"
- "prediction model"
- "classification model"
- "ML pipeline"

unless the page also names what the model is, what it learns from, what it predicts or ranks, and how it is tested.

## Site-Wide Model Detail Rule

Each topic architecture should show three model levels:

1. **Reference model:** the simple, explicit model that proves the target is defined correctly.
2. **Main candidate model:** the model that fits the data type and future use case.
3. **Challenger or advanced model:** the model to test only after the reference and validation design are credible.

Each model block should include:

- target variable or output label
- input variables or source evidence
- training unit, such as row, depth point, sample, station pair, image crop, graph edge, or action step
- split policy, such as leave-well-out, leave-region-out, chronological, leave-line-out, held-out task, or sample-held-out
- metrics
- leakage or drift risk
- human review checkpoint

## Source Vocabulary To Use

### Gas Hydrate Well-Log ML Paper

Use these details whenever North Slope, well logs, geoscience transfer, or energy screening appears:

- Target: NMR-derived gas hydrate saturation, `Sgh`.
- Inputs: bulk density, density porosity, gamma radiation `GR`, resistivity `Rt`, compressional velocity `Vp`, shear velocity `Vs`.
- Wells: Mount Elbert, Ignik Sikumi, Kuparuk 7-11-12 / Hydrate-01, Mallik 2L-38, Mallik 5L-38.
- Dataset unit: depth point.
- QC: missing log removal at corresponding depth points, caliper washout screening, GLOSS outlier detection, min-max normalization.
- Model: ANN in Keras/TensorFlow.
- Paper hyperparameter example: two hidden layers, 40 nodes per layer, learning rate 0.001, batch size 100, 500 epochs.
- Feature combinations: pair and triplet well-log combinations, especially `GR + Vp`, `Rt + Vp`, `phi + GR + Vp`, and `phi + Rt + Vp`.
- Metrics: `R2` or accuracy-style score against NMR-derived `Sgh`.
- Portfolio upgrade: show well-held-out, area-held-out, or basin-held-out validation when the claim is about transfer or deployment.

### CreditScoreV4 / ML Project Notes

Use these reliability details across every topic:

- leakage-safe `Pipeline` / `ColumnTransformer`
- transforms fit only on training data
- chronological or rolling validation for time-based data
- shift before rolling features
- metrics by task: RMSE, MAE, R2, ROC-AUC, PR-AUC, F1, calibration
- drift checks: PSI, KS, feature-level drift, missingness, score buckets, segment monitoring
- ETL quality: completeness, uniqueness, validity, consistency, timeliness, reasonableness, reconciliation
- production controls: fallback model, rollback path, manual review, vendor/source-change validation
- fairness metrics where people are affected

## Topic Model Specs

### 1. How AI Agents Learn Scientific Software

Future use case: an agent receives a scientific software task, already has the user's recordings and project files, and must execute the task in QGIS, ParaView, notebooks, or another technical workspace with review checkpoints.

**Reference model**

- Model: multinomial logistic regression or LightGBM action classifier.
- Target: next action class, such as open file, run tool, change layer, edit parameter, export output, inspect result, or request human review.
- Inputs: prompt type, rubric id, current software state label, file type, previous action, error flag.
- Training unit: one labeled action step.
- Purpose: prove the action taxonomy and labels are usable before using a larger sequence model.

**Main candidate model**

- Model: behavior-cloning transformer over action traces.
- State encoder: screenshot embedding from CLIP/SigLIP-style vision encoder plus OCR/UI element tokens plus file-tree metadata.
- Policy head: predicts action type, target UI element, tool parameter, and stop/review decision.
- Target labels: action token, UI target, parameter value, success/failure label, correction reason.
- Training unit: sequence of `observe state -> choose action -> execute -> inspect result`.

**Challenger model**

- Model: decision transformer or hierarchical agent model.
- High-level planner: LLM/tool planner creates task graph.
- Low-level controller: UI action policy executes clicks, keystrokes, file edits, and software commands.
- Retrieval layer: vector search over previous task traces, rubrics, and accepted outputs.

**Validation**

- Split: held-out task, held-out software project, held-out file structure.
- Metrics: task success rate, step accuracy, action F1, replay pass rate, unsafe action rate, human correction count.
- Failure gates: shortcut memorization, hidden state missing from recording, ambiguous rubric, destructive action, unapproved external upload.

**Diagram label**

Use: `CLIP/OCR state encoder -> behavior-cloning transformer -> replay simulator -> held-out scientific task score`.

### 2. AI + Knowledge Graphs For Critical Minerals

Future use case: an agent turns research sources into a queryable, auditable mineral-systems graph where every edge has evidence and uncertain edges are reviewed.

**Reference model**

- Model: rule-assisted transformer NER with SciBERT/MatSciBERT-style embeddings.
- Target: entity labels such as mineral, host rock, deposit, process, location, age, source, observation, interpretation.
- Inputs: thesis text, slide text, captions, CSV node tables, source notes.
- Training unit: sentence, table row, or slide text box.

**Main candidate model**

- Model: relation extraction transformer plus cross-encoder edge ranker.
- Target: edge type and confidence, such as observed, inferred, analog, conceptual, AI-suggested.
- Inputs: entity pair, source sentence/chunk, figure caption, source type, existing graph context.
- Output: source-backed edge proposal with evidence span and confidence rank.

**Challenger model**

- Model: relational GNN such as R-GCN, GraphSAGE, or Graph Attention Network.
- Alternative link-prediction models: TransE, RotatE, ComplEx for relation ranking.
- Target: candidate relationship or prospectivity edge to review, not an unsupported final claim.
- Inputs: graph nodes, edge types, evidence weights, geologic categories, source provenance.

**Validation**

- Split: held-out source document, held-out deposit, or held-out edge set.
- Metrics: entity precision/recall/F1, edge precision/recall/F1, source-citation accuracy, MRR/Hits@K for link ranking, expert acceptance rate.
- Failure gates: duplicate entities, synonym split, hallucinated edge, graph leakage, visually strong but weakly sourced relationship.

**Diagram label**

Use: `SciBERT entity extractor -> relation cross-encoder -> GraphRAG retrieval -> R-GCN/GraphSAGE edge ranking -> human edge audit`.

### 3. First AI Visualization: Earthquake Globe

Future use case: the 3D globe becomes a feature-engineering workbench where spatial/time event data is transformed into testable rows, not unsupported earthquake forecasts.

**Reference model**

- Model: Poisson GLM for event counts by region and time window.
- Target: count of events in the next window or anomaly flag for the current window.
- Inputs: prior-window count, magnitude bins, depth bins, region id, time-of-day/month, lagged features.
- Training unit: region-time window.

**Main candidate model**

- Model: negative binomial GLM if counts are overdispersed, or LightGBM/XGBoost regressor for next-window count or anomaly score.
- Inputs: lagged event counts, magnitude histogram, depth histogram, cluster density, distance-to-prior-event summaries, rolling change rates.
- Output: expected count, anomaly rank, or uncertainty band.

**Challenger model**

- Model: Hawkes process for self-exciting event sequences, ST-DBSCAN/HDBSCAN for spatiotemporal clustering, or temporal transformer only after the target is clear.
- Target: cluster membership, event-rate change, or region-window anomaly.

**Validation**

- Split: chronological split or leave-region-out split.
- Metrics: MAE/RMSE for counts, PR-AUC/F1 for rare anomaly labels, calibration for probability outputs.
- Failure gates: look-ahead leakage, random-window leakage, rare-event imbalance, visual overclaim, no forecast language without evaluated target.

**Diagram label**

Use: `USGS events -> region-time windows -> Poisson/negative-binomial count model -> LightGBM anomaly ranker -> chronological validation`.

### 4. Seismic Notebooks And Pondicherry

Future use case: notebooks become a reproducible waveform QA and arrival-picking system.

**Reference model**

- Model: logistic regression or LightGBM waveform QA classifier.
- Target: usable waveform / weak waveform / station mismatch / needs human pick.
- Inputs: SNR, distance, channel, station metadata completeness, event magnitude, expected arrival window, missingness flags.
- Training unit: event-station-channel waveform window.

**Main candidate model**

- Model: PhaseNet or EQTransformer for P/S arrival picking.
- Target: P arrival probability, S arrival probability, noise probability, pick time uncertainty.
- Inputs: three-component waveform windows and station metadata.
- Output: pick proposal plus confidence interval.

**Challenger model**

- Model: pretrained seismic representation model or CNN/Transformer waveform encoder with task heads for pick quality, event association, and waveform anomaly.
- Uncertainty model: bootstrapped LightGBM, quantile regression, or Gaussian Process regression for velocity uncertainty summaries.

**Validation**

- Split: held-out event, held-out station, or held-out region.
- Metrics: pick-time error in seconds, precision/recall for usable picks, SNR-stratified performance, velocity residual error.
- Failure gates: station mismatch, weak signal, bad metadata, uncertain manual pick, water-path/geologic interpretation overclaim.

**Diagram label**

Use: `ObsPy waveform windows -> LightGBM QA -> PhaseNet/EQTransformer picks -> bootstrap uncertainty -> reviewed velocity table`.

### 5. AI For Energy Screening Workflows

Future use case: a public-safe and expert-reviewed hydrate screening architecture for North Slope-style energy decisions.

**Reference model**

- Model: Ridge regression or ElasticNet regression for `Sgh`.
- Target: NMR-derived gas hydrate saturation `Sgh`.
- Inputs: selected logs such as `GR`, `Rt`, `Vp`, density porosity, bulk density, `Vs`, plus missingness flags.
- Training unit: depth point after QC.
- Purpose: show whether the feature table and target are coherent before flexible models.

**Main candidate model**

- Model: ANN in Keras/TensorFlow, matching the hydrate paper family.
- Architecture to show: dense feed-forward ANN, two hidden layers, 40 nodes per layer, learning rate 0.001, batch size 100, 500 epochs as a source-backed starting example.
- Target: continuous `Sgh` regression.
- Inputs: pair/triplet well-log combinations such as `GR + Vp`, `Rt + Vp`, `phi + GR + Vp`, `phi + Rt + Vp`.
- QC: missing log row removal, caliper washout screening, GLOSS outlier removal, min-max normalization fit only on training wells.

**Challenger models**

- Model: XGBoost/LightGBM regression for `Sgh`.
- Model: random forest regression for nonlinear interaction screening.
- Model: multitask neural network with one head for hydrate occurrence classification and one head for `Sgh` regression.
- Optional uncertainty: quantile regression forest, conformal prediction, or ensemble variance for abstention.

**Validation**

- Split: leave-well-out, leave-area-out, and basin-transfer test. Avoid random depth-row split for deployment claims.
- Metrics: R2, MAE, RMSE for `Sgh`; ROC-AUC, PR-AUC, F1 for occurrence head; calibration curve; abstention coverage.
- Failure gates: target leakage, random depth-row overfit, missing NMR/shear sonic, washout intervals, gas/ice/cement lookalikes, overconfident transfer.

**Diagram label**

Use: `caliper + GLOSS QC -> train-only normalization -> Ridge/ElasticNet reference -> Keras ANN Sgh regressor -> XGBoost challenger -> leave-well/basin transfer test`.

### 6. AI For Visual Geoscience Classification

Future use case: rock, mineral, and formation evidence becomes a multimodal training set with image, chemistry, and text features.

**Reference model**

- Model: logistic regression or linear SVM on hand-built features.
- Target: rock class, mineral label, formation label, or "ambiguous/needs expert review."
- Inputs: chemical ratios, spider-diagram values, simple image texture statistics, source label.
- Training unit: sample, image crop, or mapped unit.

**Main candidate model**

- Image model: EfficientNet-B0/B3, ResNet-50, or ViT fine-tuned on thin-section and map/image crops.
- Tabular model: XGBoost/LightGBM on chemistry and formation variables.
- Fusion model: late-fusion MLP that combines image embedding, tabular chemistry embedding, and source-text embedding.

**Challenger model**

- Model: CLIP/SigLIP-style image-text embedding for retrieval and weakly supervised label ranking.
- Model: Swin Transformer for higher-resolution microscopy or map image patches.

**Validation**

- Split: sample-held-out, site-held-out, or formation-held-out. Do not random-split duplicate image crops from the same sample.
- Metrics: macro-F1, balanced accuracy, top-k accuracy, confusion matrix, expert correction rate.
- Failure gates: weak label, missing scale, mixed class definition, correlated chemistry, same-sample leakage, overconfident visual label.

**Diagram label**

Use: `ResNet/EfficientNet image branch + XGBoost chemistry branch + late-fusion label ranker -> expert label audit`.

### 7. SAGE / Valles Caldera Geophysics

Future use case: AI ranks agreement and conflict zones across imperfect survey methods without flattening uncertainty.

**Reference model**

- Model: rule-based agreement score or logistic regression conflict classifier.
- Target: agree / conflict / insufficient evidence / needs review.
- Inputs: method presence flags, anomaly strength, uncertainty score, spatial overlap, source method.
- Training unit: grid cell, line intersection, or interpreted zone.

**Main candidate model**

- Model: LightGBM or random forest agreement/conflict classifier.
- Inputs: gravity anomaly, EM/TEM/ERT response, seismic velocity, mapped geology, terrain, acquisition quality, spatial registration error.
- Output: review-priority rank and conflict type.

**Challenger models**

- Model: Gaussian Process regression or co-kriging for method-specific continuous surfaces with uncertainty.
- Model: U-Net for anomaly/zone segmentation on gridded geophysical images, only when labeled examples exist.
- Model: graph neural network over survey intersections, with nodes as zones/lines and edges as spatial adjacency or method overlap.

**Validation**

- Split: leave-area-out or leave-survey-line-out.
- Metrics: conflict-label F1, review-priority precision@K, calibration of uncertainty, expert agreement rate.
- Failure gates: misregistration, acquisition artifact, method physics ignored, false consensus, smooth map overclaim.

**Diagram label**

Use: `method-specific features -> LightGBM conflict classifier -> Gaussian Process uncertainty surfaces -> expert disagreement board`.

### 8. AI For Near-Surface Geophysics

Future use case: shallow field methods are compared line-by-line, with AI ranking where methods agree or need review.

**Reference model**

- Model: logistic regression or decision tree for method-agreement status.
- Target: agreement / conflict / missing context / possible unit only.
- Inputs: line id, intersection id, velocity, resistivity, conductivity, depth, field-note completeness.
- Training unit: line intersection or depth interval.

**Main candidate model**

- Model: LightGBM classifier or random forest classifier for conflict/review ranking.
- Inputs: hammer seismic velocity, ERT resistivity, TEM conductivity, possible unit label, line geometry, depth, uncertainty flag.
- Output: review target, not final geologic unit.

**Challenger models**

- Model: Gaussian Process or Bayesian hierarchical model for method-specific property surfaces.
- Model: U-Net or shallow segmentation model for cross-section zones if labeled cross-sections exist.
- Model: graph model where nodes are method intervals and edges are line intersections.

**Validation**

- Split: leave-line-out or leave-intersection-out.
- Metrics: conflict F1, review-priority precision@K, false-consensus rate, expert acceptance.
- Failure gates: wrong intersection, field-note loss, unit-label drift, over-smoothed cross-section, unsupported final-unit label.

**Diagram label**

Use: `line geometry -> LightGBM conflict ranker -> GP method uncertainty -> leave-line-out validation -> review target`.

### 9. Supervised ML For Moho Depth Mapping

Future use case: gravity/Moho relationships are tested for regional transfer instead of only familiar-data accuracy.

**Reference model**

- Model: Ridge regression, ElasticNet, or Generalized Additive Model.
- Target: Moho depth.
- Inputs: gravity anomaly, location, topography, crustal proxy variables, region id.
- Training unit: grid cell or station/control point.

**Main candidate model**

- Model: XGBoost/LightGBM regression or random forest regression.
- Target: Moho depth with residual/error map.
- Inputs: gravity features, spatial derivatives, regional geologic context, coordinate features handled carefully.

**Challenger models**

- Model: Keras MLP/ANN regression, matching the older class-project style.
- Model: Gaussian Process regression or kriging residual model for spatial uncertainty.
- Model: neural network plus residual kriging hybrid if enough data exists.

**Validation**

- Split: leave-region-out, Australia-to-USA transfer, or spatial block validation.
- Metrics: RMSE, MAE, R2, residual bias by region, uncertainty calibration.
- Failure gates: spatial leakage, coordinate memorization, train/test boundary bias, hidden variable mismatch, high score without transfer.

**Diagram label**

Use: `Ridge/GAM reference -> LightGBM Moho regressor -> ANN challenger -> Gaussian Process residual uncertainty -> leave-region-out transfer`.

### 10. AI For Ambient-Noise Seismology

Future use case: continuous records become monitored station-pair products where AI triages which correlations are stable enough to trust.

**Reference model**

- Model: logistic regression or LightGBM CCF-quality classifier.
- Target: stable CCF / unstable CCF / data gap / instrument issue / seasonal flag.
- Inputs: stack count, CCF peak strength, symmetry, lag-time stability, SNR proxy, station-pair distance, missing windows, station metadata flags.
- Training unit: station-pair time window.

**Main candidate model**

- Model: Isolation Forest or robust PCA for station-pair anomaly detection.
- Model: LightGBM classifier for stable versus unstable station-pair outputs.
- Output: station-pair review priority, not automatic subsurface interpretation.

**Challenger models**

- Model: waveform representation model such as SeisLM-style pretrained embedding with a task head for station-pair quality or change detection.
- Model: LSTM/temporal convolution/temporal transformer for CCF time series after stable labels exist.
- Model: Bayesian online change-point detection for monitoring shifts.

**Validation**

- Split: held-out station pair, held-out time period, or held-out network.
- Metrics: precision/recall for flagged bad windows, false alert rate, detection delay, stability score calibration.
- Failure gates: weak correlation treated as signal, seasonal noise, station metadata error, instrument change, late or missing data.

**Diagram label**

Use: `CCF feature table -> LightGBM stability classifier -> Isolation Forest anomaly triage -> SeisLM embedding challenger -> human alert review`.

### 11. AI App Building, Automation, And Model Risk

Future use case: a Codex-built app shows how to make prediction-like dashboards without hiding leakage, stale data, or drift.

**Reference models**

- Time-series reference: persistence model, such as tomorrow equals today or next return equals zero.
- Smoother reference: moving-average or exponentially weighted moving average for volatility/level.
- Classification reference: logistic regression on past-only rolling features for up/down or risk bucket target.

**Main candidate models**

- Model: ElasticNet regression for continuous target such as next-window return, volatility, or drawdown risk.
- Model: XGBoost/LightGBM classifier or regressor using past-only rolling features.
- Model: calibrated classifier with Platt scaling or isotonic calibration when probabilities are shown.

**Challenger models**

- Model: ARIMA/SARIMAX for single-series time forecasting when target is a level or volatility measure.
- Model: temporal convolution/LSTM only after walk-forward validation proves a simpler model is insufficient.
- Model-risk analogy: CreditScoreV4-style drift monitor with feature-level PSI, missingness, score buckets, segment metrics, fallback path.

**Validation**

- Split: walk-forward or rolling chronological split.
- Metrics: MAE/RMSE for continuous targets, ROC-AUC/PR-AUC/F1/Brier score for classification, calibration curve, drift PSI, stale-data flag.
- Failure gates: future leakage, no persistence reference, stale refresh, ticker universe bias, survivorship bias, overclaiming investment usefulness.

**Diagram label**

Use: `persistence + moving-average references -> ElasticNet/LightGBM challenger -> walk-forward validation -> PSI drift monitor -> claim-language gate`.

### 12. AI For SEM Petrography And Climate Proxies

Future use case: SEM images become reviewable visual labels while proxy interpretations remain blocked until supported by expert and literature evidence.

**Reference model**

- Model: linear SVM or logistic regression on image texture features.
- Target: visible label, such as grain, pore/fracture, clay morphology, mineral texture, or ambiguous.
- Inputs: texture features, scale metadata, crop location, sample id.
- Training unit: image crop.

**Main candidate models**

- Model: EfficientNet or ResNet patch classifier for visible labels.
- Model: U-Net or Mask R-CNN for grain/pore/fracture segmentation when pixel labels exist.
- Model: CLIP/SigLIP embedding retrieval for finding similar expert-labeled examples.

**Challenger models**

- Model: ViT/Swin Transformer for high-resolution microscopy labels.
- Model: retrieval-augmented LLM claim reviewer that checks whether a proxy claim has literature/source support. This is not allowed to infer climate interpretation from image pixels alone.

**Validation**

- Split: sample-held-out or site-held-out. Do not random-split crops from the same SEM image into train and test.
- Metrics: macro-F1 for patch labels, IoU/Dice for segmentation, top-k retrieval accuracy, expert acceptance rate, unsupported-claim block rate.
- Failure gates: texture overclaim, detrital/authigenic confusion, missing scale, proxy claim from image alone, literature mismatch.

**Diagram label**

Use: `EfficientNet/ResNet patch classifier -> U-Net/Mask R-CNN segmentation -> CLIP retrieval -> literature-backed proxy claim gate`.

## Replacement Wording For Website Copy

Use the right-side wording instead of the vague left-side wording.

| Vague wording | Replace with |
| --- | --- |
| baseline model | Ridge regression, ElasticNet, logistic regression, Poisson GLM, persistence forecast, or rule-based agreement score, depending on the topic |
| ML model | Keras ANN, LightGBM, XGBoost, PhaseNet, EQTransformer, GraphSAGE, R-GCN, U-Net, Isolation Forest, Gaussian Process, or EfficientNet |
| model validation | leave-well-out, basin-transfer, chronological walk-forward, leave-line-out, held-out task replay, sample-held-out, or leave-region-out validation |
| prediction | `Sgh` regression, occurrence classification, arrival-pick time, CCF stability, Moho depth, edge ranking, action replay, or review-priority ranking |
| uncertainty | calibration curve, ensemble variance, conformal interval, Gaussian Process posterior, bootstrap interval, pick-time uncertainty, or abstention coverage |
| data quality | caliper washout, GLOSS outlier detection, missingness, CRS mismatch, station metadata error, line geometry error, duplicate timestamps, source provenance |

## Build Priority

1. North Slope hydrate: most source-backed model detail, using ANN/Keras, `Sgh`, well-log combinations, caliper/GLOSS QC, and leave-well/basin validation.
2. Agent scientific software: most important future-agent story, using screenshot/OCR state encoder, behavior-cloning transformer, replay validation.
3. Knowledge graph: strongest non-numeric ML story, using SciBERT entity extraction, relation cross-encoder, GraphRAG, and GraphSAGE/R-GCN edge ranking.
4. Stock app risk: clearest production-risk analogy, using persistence reference, ElasticNet/LightGBM, walk-forward validation, PSI drift, fallback model.
5. Ambient noise: strongest continuous-data pipeline, using LightGBM CCF quality, Isolation Forest anomaly detection, SeisLM-style embeddings.
6. Geophysics disagreement: most important field-science credibility story, using LightGBM conflict ranking, Gaussian Process uncertainty, and leave-line/area validation.

## Completion Definition

A topic is model-detailed only when it names:

- model class
- target
- input variables
- training unit
- split policy
- metrics
- leakage/drift/error gate
- human review step
- exact diagram wording
