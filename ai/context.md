# Laser Resonator Beam Alignment Project Context

## Project Overview

This project focuses on laser resonator beam alignment using metadata-only data. The original concept involved before/after beam images, but the current available data contains no images. The available files are:

- `labels.json`: beam-state records with beam measurements, Gaussian fit information, controllable alignment parameters, and metadata.
- `sampled_pairs_500k.json`: sampled before/after state index pairs with `diff_count`, the number of changed controllable parameters.

The goal is to help an operator move from a current before state to a desired after state by predicting the required changes to four controllable alignment parameters.

## Controllable Parameters

The four controllable parameters are:

- `Iris Position`
- `Z Position`
- `Pitch Position`
- `Yaw Position`

## Example Beam State

Each entry in `labels.json` represents one beam state. A state includes metadata such as date, timestamp, experiment number, Gaussian equation strings, beam-quality measurements, current parameter positions, power, exposure time, and filename.

Important example fields include:

- `X Axis Gaussian Equation`
- `Y Axis Gaussian Equation`
- `Gaussian Fit % along X`
- `Gaussian Fit % along Y`
- `X Axis Centroid`
- `Y Axis Centroid`
- `Major Axis Beam Width`
- `Minor Axis Beam Width`
- `Effective Diameter`
- `Ellipticity`
- `Iris Position`
- `Z Position`
- `Pitch Position`
- `Yaw Position`
- `Power Measurement`
- `Exposure Time`

## Pair Dataset

Each entry in `sampled_pairs_500k.json` contains:

- `index1`: index of the before state in `labels.json`
- `index2`: index of the after state in `labels.json`
- `diff_count`: number of controllable parameters changed between the two states

Possible `diff_count` values are `0`, `1`, `2`, `3`, and `4`.

## Input Design

The model input should include:

- before-state beam-quality and shape metadata,
- before-state current parameter values,
- desired after-state beam-quality and shape metadata.

The model should not use after-state parameter values as input, because those are the values the model is trying to infer indirectly through predicted deltas.

The desired after state is assumed to be available at inference time for the first project version.

## Excluded Metadata

The following fields should not be used as direct model features unless a later analysis gives a clear reason:

- `Date`
- `Timestamp`
- `Experiment Number`
- `filename`

These fields may still be useful for grouping, splitting, audit trails, and leakage checks.

## Candidate Beam Features

The initial candidate feature set should include beam-quality and shape fields such as:

- Gaussian fit percentages along X and Y,
- centroids,
- beam widths,
- effective diameter,
- ellipticity,
- parsed Gaussian equation parameters.

`Power Measurement` and `Exposure Time` should be treated as candidate features. Their relevance should be decided through EDA, correlation analysis, leakage checks, and ablation tests.

## Gaussian Equation Parsing

The Gaussian equation strings should be parsed into numeric features instead of being discarded.

For equations such as:

```text
Aexp[-2([x-5758]/995)^2]
```

candidate parsed values include:

- Gaussian center, for example `5758`,
- Gaussian width/scale, for example `995`.

Parsed Gaussian values should be evaluated during EDA. They may be kept alongside centroid and beam-width fields initially, but EDA should decide whether they add useful signal or are redundant.

## Target Design

The target is the delta for each controllable parameter:

```text
delta = after_parameter_value - before_parameter_value
```

The model should predict amount and direction of change for:

- `Iris Position`
- `Z Position`
- `Pitch Position`
- `Yaw Position`

Delta values should be rounded to 3 decimal places.

## Change Detection Rule

A parameter should be considered changed based on its value rounded to 3 decimal places.

Examples:

- `2.755` and `2.756` are different.
- `2.755` and `2.7551` are treated as equal after rounding to 3 decimal places.

Both change labels and delta regression targets should use this 3-decimal convention.

## Prediction Structure

The initial model design should use a two-stage structure:

1. Predict which parameters changed.
2. Predict delta values only for the parameters predicted as changed.

For final output, all four parameter deltas should be returned. Parameters predicted as unchanged should be returned as `0.000`.

Example output shape:

```json
{
    "Iris Position delta": 0.0,
    "Z Position delta": 0.0,
    "Pitch Position delta": 0.35,
    "Yaw Position delta": -0.1
}
```

For now, the output should be numeric deltas only. Human-readable operator instructions can be added later.

## Role of `diff_count`

`diff_count` tells how many parameters changed, but not which parameters changed. Therefore, it is not sufficient as the main target.

The model still needs to identify the specific changed parameters when `diff_count > 0`.

`diff_count` should be used during testing/evaluation as a consistency check. For example, the number of predicted changed parameters can be compared against the ground-truth `diff_count`.

The data is assumed to be consistent, so preprocessing does not need to resolve conflicts between derived changed-parameter labels and `diff_count`.

## Primary Evaluation Priority

The most important evaluation goal is accurate delta prediction after changed parameters are identified.

Parameter-change identification is required, but the main success criterion is whether the predicted adjustment amounts and directions are accurate for the changed parameters.

## EDA-First Approach

The project should begin with EDA before modeling.

EDA should answer:

- Which features are relevant for predicting parameter deltas?
- Are there data quality issues, missing values, outliers, or malformed Gaussian equations?
- What are the distributions of beam features and controllable parameters?
- What are the distributions of target deltas?
- How balanced are the classes across `diff_count` values?
- How balanced are the changed-parameter combinations?
- Are `Power Measurement` and `Exposure Time` useful or potentially misleading?
- Are parsed Gaussian features useful or redundant?
- Are there correlations or dependencies between parameters and beam metadata?
- What are the observed min/max ranges for each parameter and delta?

### EDA Validation of Two-Stage Architecture

EDA should include baseline benchmarking of both stages of the two-stage architecture:

1. **Classification Benchmarks**: Baseline Random Forest classifiers to validate that parameter-change detection is feasible with the current feature set.
2. **Regression Benchmarks**: Baseline Random Forest regressors to validate that delta prediction is feasible and that the feature set supports accurate magnitude/direction predictions.

This dual validation ensures both stages of the architecture are viable before proceeding to detailed feature engineering and train/val/test splitting.

## Feature Engineering Plan

Initial modeling features should include absolute before-state and desired after-state features.

The first design should not rely only on engineered feature differences because the relationship between beam metadata and parameter changes is not yet known.

Recommended starting feature blocks:

- before beam features,
- before current parameter values,
- desired after beam features,
- parsed Gaussian numeric features for before and after states.

Optional features for EDA or ablation:

- after-minus-before beam feature differences,
- feature ratios,
- normalized differences,
- interaction features between before parameters and desired beam state.

## Initial Modeling Approach

Start with classical ML. Deep learning should be considered later only if classical methods are insufficient.

The preferred initial design is separate per-parameter models:

- one classifier per parameter to predict whether that parameter changed,
- one regressor per parameter to predict the delta when that parameter changed.

This gives eight initial model components:

- Iris changed classifier
- Iris delta regressor
- Z changed classifier
- Z delta regressor
- Pitch changed classifier
- Pitch delta regressor
- Yaw changed classifier
- Yaw delta regressor

This approach is preferred initially because it improves interpretability, feature-importance analysis, debugging, and per-parameter error analysis.

A multi-output model can be explored later if separate models fail to capture coupling between parameters.

## Candidate Classical Models

Candidate models for the first experiments include:

- random forest classifiers/regressors,
- gradient boosting models,
- XGBoost/LightGBM/CatBoost if available,
- regularized linear/logistic baselines,
- small MLP baseline if needed later.

Tree-based models are especially suitable for the first phase because they handle nonlinear relationships and offer feature-importance tools.

## Data Splitting Strategy

Use both random and grouped splits, then compare results.

### Random Split

Use a 70/15/15 train/validation/test split by sampled pair.

Purpose:

- optimistic baseline,
- checks interpolation within the known pair distribution,
- easier to balance and compare early models.

Risk:

- may leak similar states, experiments, or operating conditions across train and test,
- may overestimate real-world performance.

### Grouped Split

Use a 70/15/15 train/validation/test split grouped by `Experiment Number`.

Purpose:

- primary generalization benchmark,
- evaluates performance on unseen experiments,
- gives a more realistic estimate for future deployment.

Risk:

- may produce harder metrics,
- may create class imbalance across splits,
- may be sensitive to the number and diversity of experiments.

The grouped split should be treated as the more honest evaluation. The random split should be reported as a secondary benchmark.

## Evaluation Metrics

Recommended evaluation metrics include:

### Change Detection

- per-parameter precision, recall, and F1,
- macro and weighted F1 across parameters,
- exact changed-set accuracy,
- predicted changed-count accuracy using `diff_count`.

### Delta Regression

For changed parameters:

- MAE per parameter,
- RMSE per parameter,
- median absolute error,
- sign accuracy for delta direction,
- tolerance-based accuracy, for example within 0.01, 0.05, or 0.10 depending on practical needs.

### End-to-End Output

- four-parameter vector MAE,
- exact zero/nonzero pattern match,
- combined score that penalizes wrong changed-parameter detection and inaccurate deltas.

## Physical Constraints

Known physical limits for parameter values are not currently available.

Therefore, the first design should not clip predictions to physical ranges. EDA should report observed ranges for:

- each parameter value,
- each parameter delta,
- each beam-quality feature.

Physical limits can be added later when available.

## Current Assumptions

- No images are available in the current phase.
- Desired after-state beam metadata is available at inference time.
- After-state parameter values are not available at inference time.
- Targets are parameter deltas, not raw final parameter values.
- Deltas and changed/not-changed labels use 3-decimal rounding.
- `diff_count` is used for evaluation consistency, not as the only target.
- Data is assumed to be internally consistent.
- EDA comes before modeling.
- Classical ML is the starting point.
- Separate per-parameter classifier/regressor models are the first modeling design.
- Both random and grouped 70/15/15 splits should be evaluated.

## Open Questions and Future Extensions

Future work may include:

- collecting or integrating actual before/after beam images,
- moving from metadata-only models to image plus metadata models,
- adding physical parameter limits and clipping rules,
- converting numeric deltas into human-readable operator instructions,
- testing multi-output models to capture coupling between parameters,
- testing deep learning models if classical ML is not sufficient,
- defining practical tolerance thresholds for successful alignment recommendations,
- identifying whether `Power Measurement` and `Exposure Time` should remain in the final feature set,
- validating whether parsed Gaussian features improve performance,
- creating an operator-facing interface for entering current and desired beam metadata.

## First Implementation Milestones

1. Load and validate `labels.json` and `sampled_pairs_500k.json`.
2. Join before/after pair records using `index1` and `index2`.
3. Parse Gaussian equation strings into numeric features.
4. Build rounded parameter deltas and changed-parameter labels.
5. Run EDA on data quality, distributions, class balance, feature relevance, and target behavior.
6. Create random 70/15/15 split.
7. Create grouped 70/15/15 split by `Experiment Number`.
8. Train baseline per-parameter classifiers and regressors.
9. Evaluate change detection, delta regression, and end-to-end output quality.
10. Compare random split vs grouped split results.
11. Use findings to refine features and decide whether more advanced models are needed.
