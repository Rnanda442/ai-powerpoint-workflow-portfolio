# North Slope ML Handoff Base

Date prepared: 2026-06-12

This is the working base for the Alaska North Slope gas hydrate Streamlit app, slides, and document work. It is not for the AI portfolio site.

## Boundary Rules

- Treat this as a public-source planning scaffold until approved runtime data is available.
- Do not place restricted well identifiers, credentials, approved-environment-only logs, populated model outputs, or sensitive derived outputs in the public repo.
- Keep target fields locked out of predictors: `S_h`, `Sgh`, `NMR_SAT`, phase labels, final rankings, and post-outcome interpretations should supervise or score models, not become input features.
- Explain every ML model in plain language before using the model name.
- Prefer complete-well or grouped-well validation. Do not use random row splits for depth-sampled log data because neighboring rows leak information.
- Show caveats beside claims: washout, missing NMR/shear sonic, depth mismatch, gas/ice/cement lookalikes, shale/carbonate effects, salinity, compaction, stress, and overburden context.

## Confirmed Email Sources

- Gmail message `19eb8291ad5c05c9`, subject `ML sources`, sent 2026-06-11 14:29 CDT.
  - `s10596-022-10151-9.pdf`
  - `ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`
- Gmail message `19eb912268782bbc`, subject `north slope of alaska powerpoint vizuals`, sent 2026-06-11 18:43 CDT.
  - Inline image 01 is the strongest data/header scaffold.
  - Inline image 04 is useful intro context.
  - Inline image 08 is a cover/title slide candidate.
  - Inline images 05, 06, and 07 are personal/about-me assets, not North Slope ML evidence.
- Gmail message `19eba86da8752830`, subject `New pressy`, sent 2026-06-12 01:30 CDT.
  - `GMAIL VISUAL REVISION 9-SLIDE North Slope Gas Hydrate Slides 2026-06-11.pptx`

## Local Source Files To Keep Ready

Primary ML paper:

- `C:\Users\gargi\Downloads\s10596-022-10151-9.pdf`
- Title: `Application of machine learning to characterize gas hydrate reservoirs in Mackenzie Delta (Canada) and on the Alaska north slope (USA)`
- Authors shown in PDF: Leebyn Chong, Harpreet Singh, C. Gabriel Creason, Yongkoo Seol, Evgeniy M. Myshakin.
- Use for: hydrate saturation ML, well-log feature combinations, ANN/Keras-style model reference, Alaska North Slope/Mackenzie transfer framing, and Sgh prediction language.

General ML reliability notes:

- `C:\Users\gargi\Downloads\ML_Project_Reference_and_CreditScoreV4_Case_Notes.docx`
- Use for: baseline-first modeling, validation schemes, leakage-safe pipelines, VIF/multicollinearity, ETL checks, drift triage, dashboards, fallback models, fairness/segment monitoring, and incident-response style explanation.

North Slope scaffold docs:

- `C:\Users\gargi\Downloads\Alaska_North_Slope_Wireline_ML_Project_Blueprint_outline.docx`
- Use for: project thesis, approved runtime data contract, staged classification/regression/sweet-spot workflow, well-log panel requirements, validation report requirements, and public/private boundary rules.
- `C:\Users\gargi\Downloads\UPDATED North Slope Gas Hydrate Reservoir Characterization Research Overview.docx`
- Use for: goal/vision language, abstract/introduction, research framing, parameter section, and story flow.

Curated source library index:

- `assets/drive_sources/north_slope_source_library/source_manifest.csv`
- `assets/drive_sources/north_slope_source_library/source_index.md`
- Note: raw library files are intentionally not tracked because the Drive ZIP and some PDFs are large. Use the tracked index for repo/app source display, and keep raw source files local or in approved cloud storage.

## Selected Visuals For The Next App Pass

Copied into `deliverables/north_slope_app_scaffold/selected_visuals/`:

- `well_log_header_scaffold.png`: best header/data-format reference.
- `parameter_signal_caveat_grid.png`: best parameter explanation block.
- `equations_become_ml_features.png`: best equation screenshot.
- `ml_workflow_model_ladder.png`: best workflow/model explanation slide.
- `errors_validation_masking_review.png`: best error/caveat/validation slide.

Source originals:

- `assets/gmail_updates/2026-06-11/north_slope_powerpoint_visuals/north_slope_email_inline_01.png`
- `assets/drive_slide_thumbnails/north_slope_parameter_grid_slide.png`
- `assets/drive_slide_candidates/north_slope_slide_05_equations_features.png`
- `assets/drive_slide_candidates/north_slope_slide_06_model_ladder.png`
- `assets/drive_slide_candidates/north_slope_slide_08_errors_validation.png`

## Incoming Data Header Format

The app scaffold should expect configurable aliases because field names will vary by exported Excel sheet, well-log table, and approved runtime source.

Required identity/context fields:

- `well_id` or approved well alias
- `depth_md` and/or `depth_tvd`
- `formation` or interval/zone where available
- `source_file`, `source_sheet`, `unit_system`, and provenance fields

Measured log/input families:

- `GR`: gamma ray, API; lithology/shale-volume support.
- `Rt`: deep resistivity, ohm-m; hydrate signal support but not standalone hydrate evidence.
- `RHOB` or `rho_b`: bulk density; density porosity and elastic feature input.
- `phi_den`: density-derived porosity.
- `phi_nmr`: NMR porosity where available.
- `Vp` and `Vs`, or source slowness fields `DT` and `DTS`.
- `CAL` or `DC`: caliper/differential caliper for borehole quality and washout flags.
- `core_porosity`, `core_permeability`, `core_lithology`, or equivalent core-calibration fields where approved.
- `pressure`, `temperature`, `overburden`, or stability/context fields where approved.

Locked target/calibration fields:

- `S_h`, `Sgh`, `NMR_SAT`, phase labels, final model labels, final rankings, and post-interpretation results.
- These can train, calibrate, score, or validate. They should not be fed back into input feature generation.

## Equation Screenshot Content To Preserve

From `equations_become_ml_features.png`:

- `Vsh = clip((GR - GR_clean) / (GR_shale - GR_clean), 0, 1)`
- `phi_den = clip((rho_ma - RHOB) / (rho_ma - rho_fl), 0, 0.70)`
- `Vp = 304.8 / DT`
- `Vs = 304.8 / DTS`
- `Vp/Vs = Vp / Vs`
- `mu-rho = rho_b * Vs^2`
- `AI = rho_b * Vp`
- `lambda-rho = rho_b * (Vp^2 - 2Vs^2)`
- `K = rho_b * (Vp^2 - 4/3Vs^2)`
- `Delta_NMR = phi_den - phi_nmr`
- `NMR_H = clip(Delta_NMR / phi_den, 0, 1)`
- `H_proxy = clip(1 - sqrt(Sw_ref / (phi_den^2 * Rt)), 0, 1)`

Important explanation: these equations make model inputs and screens. They are not final hydrate labels by themselves.

## ML Model Language To Use

Plain-English model ladder:

- Rules and baselines: transparent references that show whether ML is actually adding value.
- Logistic/linear models: simple, explainable baselines for occurrence or saturation trends.
- Random Forest / Gradient Boosting / XGBoost: tabular models that learn nonlinear relationships between GR, Rt, porosity, sonic, density, and context fields.
- ANN/Keras model: a neural network challenger based on the Chong et al. hydrate paper; useful only if grouped-well validation improves and uncertainty is controlled.
- Ensemble/review layer: combines model outputs with uncertainty flags and geologist review rather than making a one-number claim.

Validation language:

- Classification outputs: hydrate-bearing, non-hydrate, mixed/uncertain, or review-needed intervals.
- Regression outputs: calibrated saturation or proxy score with MAE, RMSE, R2, residual plots by well and interval.
- Required guardrail: fit scalers, imputers, encoders, feature selectors, and thresholds only on training wells, then apply them to held-out wells.

## Next Build Order

1. Goal and vision block.
2. Well-log scaffold block using the header format above.
3. Equations-to-features block using the selected equation screenshot.
4. Model ladder block with plain-English model cards.
5. Errors, validation, and masking review block.
6. Source index panel that references the curated source library without shipping large raw documents.

