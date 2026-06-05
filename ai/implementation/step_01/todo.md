# Step 1 Todo: Data Ingestion & Preprocessing

This checklist is grouped into execution units that can move through the sprint flow together. Units are ordered by dependency, but each unit has a clear review boundary and artifact expectation.

## Backlog

_(Sub-tasks for future steps or overflow from the current step)_

## To Do

## In Progress

## In Review

## Done

### Unit 01 - Notebook Scaffold and Run Context

- Created `notebooks/01_data_ingestion_and_prep.ipynb`.
- Defined project-root-relative paths in the notebook.
- Added a notebook structure matching the Step 1 flow: load, validate, join, parse, synthesize targets, resolve missing values, validate output, save CSV.
- Verified the notebook JSON parses successfully.

### Unit 02 - Raw Data Loading and Schema Validation

- Confirm expected raw data paths:
    - `data/raw/labels.json`
    - `data/raw/sampled_pairs_500k.json`
- Write and run Python code in the Step 1 notebook to load both raw files.
- Inspect shapes, sample records, field names, and basic schema characteristics through notebook/Python output.
- Validate fields required for pair joining, candidate features, Gaussian parsing, target synthesis, and metadata retention through notebook/Python code.
- Document any schema assumptions or unexpected raw-field issues in the notebook.
- Do not rely on model-side/manual inspection of raw JSON files as the source of truth for Unit 02.

### Unit 03 - Pair Join and Role-Based Column Layout

- Joined before/after states using `index1` and `index2`.
- Renamed columns with role prefixes: `before_`, `after_`, and `meta_`.
- Kept required metadata columns (`meta_index1`, `meta_index2`, `meta_before_experiment_number`, `meta_after_experiment_number`, `meta_diff_count`).
- Kept before-state controllable parameter columns as model input features.
- Dropped direct date/time/file metadata (`Date`, `Timestamp`, `filename`) from the final CSV.

### Unit 04 - Gaussian Parsing and Raw String Cleanup

- Parsed before/after X/Y Gaussian equation strings into numeric center and scale fields (`before_x_gaussian_center_parsed`, `before_x_gaussian_scale_parsed`, etc.).
- Reported 0 parse failures across all 500,000 pairs (all parsed successfully).
- Dropped raw Gaussian equation string columns from the joined dataset.
- Promoted `parse_gaussian_equation()` and `parse_gaussian_dataframe()` into `src/features/gaussian_parser.py`.

### Unit 05 - Target Synthesis and Leakage Checks

- Computed the four target delta columns using raw numeric values and standard Python/pandas 3-decimal rounding.
- Computed the four binary changed-label columns.
- Excluded rows with missing required target-synthesis values (none found).
- Dropped after-state controllable parameter columns to avoid leakage.
- Validated `meta_diff_count` against synthesized changed labels (0 mismatches).
- Promoted target synthesis functions into `src/features/targets.py`.

### Unit 06 - Missing-Value Resolution and Final CSV Validation

- Inspect missing values by column.
- Choose and document an explicit missing-value strategy (sentinel imputation for beam metrics, median for Gaussian features).
- Verify the final dataset has no missing values.
- Save exactly one processed CSV: `data/processed/dataset_001.csv` (500,000 rows, 45 columns).
- Confirm the saved CSV is unsplit and ready for Step 2 EDA.

### Unit 07 - End-of-Step Review and Promotion Decision

- Reviewed validated notebook helper logic and promoted into `src/`:
    - `src/features/gaussian_parser.py`: Gaussian equation parsing (0 failures, 100% success)
    - `src/features/targets.py`: Delta computation and changed-label synthesis
    - `src/data/load_data.py`: Data loading utilities
- Verified final dataset: 500,000 rows, 45 columns, 0 missing values
- All validation checks passed (7/7)
- Updated `ai/implementation/step_01/outcome.md` with complete documentation
