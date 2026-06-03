# Step 1 Todo: Data Ingestion & Preprocessing

## Backlog

- Create `notebooks/01_data_ingestion_and_prep.ipynb`.
- Confirm expected raw data paths:
  - `data/raw/labels.json`
  - `data/raw/sampled_pairs_500k.json`
- Load both raw files and inspect shapes, sample records, and required fields.
- Validate required fields for pair joining, beam features, Gaussian parsing, target synthesis, and metadata retention.
- Join before/after states using `index1` and `index2`.
- Rename columns with role prefixes: `before_`, `after_`, `target_`, and `meta_`.
- Parse before/after X/Y Gaussian equation strings into numeric center and scale fields.
- Drop raw Gaussian equation string columns after parsing.
- Compute the four target delta columns using raw numeric values and standard Python/pandas 2-decimal rounding.
- Compute the four binary changed-label columns.
- Drop after-state controllable parameter columns after target synthesis.
- Keep before-state controllable parameter columns as model input features.
- Keep required metadata columns:
  - `meta_index1`
  - `meta_index2`
  - `meta_before_experiment_number`
  - `meta_after_experiment_number`
  - `meta_diff_count`
- Drop direct date/time/file metadata from the final CSV:
  - `Date`
  - `Timestamp`
  - `filename`
- Report Gaussian parse failure counts.
- Inspect missing values by column.
- Choose and document an explicit missing-value strategy.
- Exclude rows with missing required target-synthesis values; never impute targets.
- Ensure the final CSV has no missing values.
- Validate `meta_diff_count` against synthesized changed labels and report warnings if mismatches exist.
- Save exactly one processed CSV:
  - `data/processed/dataset_001.csv`
- Confirm the saved CSV is unsplit and ready for Step 2 EDA.
- Review whether any validated helper logic should be promoted into `src/`.

## In Progress

-

## In Review

-

## Done

-
