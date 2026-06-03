# Step 1 Explainer: Data Ingestion & Preprocessing

## Purpose

Step 1 prepares the raw metadata into one complete, unsplit, EDA-ready and model-ready CSV dataset. The agent writes executable notebook code to perform the preparation; it must not manually assemble the CSV.

The primary notebook artifact is:

```text
notebooks/01_data_ingestion_and_prep.ipynb
```

The primary data artifact produced by running the notebook is:

```text
data/processed/dataset_001.csv
```

## Scope

Step 1 includes:

- loading `data/raw/labels.json`,
- loading `data/raw/sampled_pairs_500k.json`,
- validating required raw fields,
- joining before/after beam states using `index1` and `index2`,
- parsing X/Y Gaussian equation strings into numeric features,
- synthesizing target deltas for the four controllable parameters,
- creating binary changed/not-changed target labels,
- resolving missing values so the final CSV has no missing values,
- saving exactly one processed CSV file.

Step 1 does not include:

- train/validation/test splitting,
- EDA conclusions,
- model training,
- model evaluation,
- operator-facing recommendation text.

Data splitting belongs to Step 3.

## Output Dataset Rules

The final CSV must be one complete dataset for Step 2 EDA. It should use role-based column prefixes:

- `before_`: current-state input features,
- `after_`: desired-state beam metadata input features,
- `target_`: synthesized target deltas and binary changed labels,
- `meta_`: audit, grouping, raw index, and evaluation-support fields.

The final CSV must keep before-state controllable parameter values as model input features:

- `before_iris_position`
- `before_z_position`
- `before_pitch_position`
- `before_yaw_position`

The final CSV must exclude after-state controllable parameter values after target synthesis because they are redundant and create leakage risk.

## Metadata Rules

The final CSV should keep the following non-feature metadata columns:

- `meta_index1`
- `meta_index2`
- `meta_before_experiment_number`
- `meta_after_experiment_number`
- `meta_diff_count`

These columns are retained for audit, EDA, consistency checks, and downstream split analysis. They are not direct model input features.

The final CSV should drop:

- `Date`
- `Timestamp`
- `filename`
- raw Gaussian equation string columns.

Grouped splitting by `Experiment Number` is a downstream assumption to validate. Before and after experiment numbers may differ, so Step 1 must preserve both experiment columns and Step 2/3 should inspect whether experiment-based grouped splitting is conceptually valid.

## Gaussian Parsing

Raw Gaussian equation strings should be parsed into numeric features for both before and after states.

Parsed fields should keep the state prefix and use `parsed` as a suffix marker. Example names:

- `before_x_gaussian_center_parsed`
- `before_x_gaussian_scale_parsed`
- `before_y_gaussian_center_parsed`
- `before_y_gaussian_scale_parsed`
- `after_x_gaussian_center_parsed`
- `after_x_gaussian_scale_parsed`
- `after_y_gaussian_center_parsed`
- `after_y_gaussian_scale_parsed`

If a Gaussian equation cannot be parsed:

- keep the row initially,
- set parsed values to missing,
- report parse failure counts in the notebook,
- inspect the failure pattern during Step 1,
- choose and document an explicit cleanup or imputation strategy before saving.

The final CSV must not contain missing values.

## Missing Value Strategy

Step 1 must inspect missing values before choosing a resolution strategy. The notebook should report missingness by column and then apply an explicit documented choice.

Recommended options:

- If missingness is tiny and caused by malformed rows, row dropping is acceptable if it does not distort target distributions.
- If parsed Gaussian values are missing but related beam measurements are present, consider median imputation or a documented derived fallback.
- If an entire candidate feature column has high missingness, consider excluding that feature from the final CSV and documenting why.
- If required target fields are missing, do not impute targets.
- If metadata needed for audit or downstream grouping is missing, inspect and resolve before saving.

Rows with missing before/after controllable parameter values required for target synthesis must be excluded from the final CSV. Target values must never be imputed.

## Target Synthesis

The four controllable parameters are:

- `Iris Position`
- `Z Position`
- `Pitch Position`
- `Yaw Position`

Target deltas should be computed from the original raw numeric values first, then rounded to 2 decimals using standard Python/pandas rounding:

```text
target_delta = round(after_raw_value - before_raw_value, 2)
target_changed = 1 if target_delta != 0.00 else 0
```

Target delta columns:

- `target_iris_delta`
- `target_z_delta`
- `target_pitch_delta`
- `target_yaw_delta`

Target changed-label columns must be numeric binary `0`/`1`:

- `target_iris_changed`
- `target_z_changed`
- `target_pitch_changed`
- `target_yaw_changed`

Step 1 should validate `meta_diff_count` by comparing it against the number of synthesized changed labels. If mismatches exist, report a warning and examples in the notebook. Do not automatically exclude mismatched rows unless a serious data integrity issue is discovered and explicitly decided during Step 1 execution.

The final CSV does not need a derived `target_changed_count` column unless later analysis requires it.

## Candidate Features

The final CSV should include before and after beam-quality/shape metadata as candidate features, including:

- Gaussian fit percentages along X and Y,
- centroids,
- major/minor beam widths,
- effective diameter,
- ellipticity,
- parsed Gaussian centers and scales,
- `Power Measurement`,
- `Exposure Time`.

`Power Measurement` and `Exposure Time` should remain candidate features for Step 2 EDA to evaluate.

## Notebook Expectations

The notebook should be readable and reproducible. It should:

- define paths relative to the project root,
- load raw files through notebook/Python code,
- inspect basic shapes, sample records, field names, and required columns through notebook/Python output,
- perform the before/after join,
- parse Gaussian fields,
- synthesize targets,
- apply missing-value resolution,
- verify the final dataset has no missing values,
- verify no after-state controllable parameter columns remain,
- verify one CSV is written to `data/processed/dataset_001.csv`.

Everything must be performed through Python code in the notebook. The agent should not rely on manual/model-side inspection of raw JSON files as the source of truth.

Small helper functions in `src/` are allowed if they make the notebook cleaner. Full production pipeline code should only be promoted after the notebook output is validated.

## End-of-Step Review

At the end of Step 1, review whether stable preprocessing logic should be promoted into `src/`. Promotion is allowed only after the notebook-generated CSV is validated, and only for reusable logic such as loading, Gaussian parsing, target synthesis, and CSV writing.
