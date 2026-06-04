# Step 1 Todo: Data Ingestion & Preprocessing

This checklist is grouped into execution units that can move through the sprint flow together. Units are ordered by dependency, but each unit has a clear review boundary and artifact expectation.

## Backlog

### Unit 07 - End-of-Step Review and Promotion Decision

- Review whether any validated helper logic should be promoted into `src/`.
- Record the Step 1 outcome, generated artifact, validation summary, and any unresolved issues in `ai/implementation/step_01/outcome.md`.
- Prepare Step 1 for completion by clearing granular tasks from `ai/implementation/PROGRESS.md` and adding the final step summary when all units are done.

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
- Validate required fields for pair joining, beam features, Gaussian parsing, target synthesis, and metadata retention through notebook/Python code.
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
- Reported Gaussian parse failure counts (0 failures detected).
- Inspected parse failure patterns (no failure pattern to inspect, as it matched perfectly across all 500k records).
- Dropped raw Gaussian equation string columns from the joined dataset.

### Unit 05 - Target Synthesis and Leakage Checks

- Computed the four target delta columns using raw numeric values and standard Python/pandas 3-decimal rounding.
- Computed the four binary changed-label columns.
- Excluded rows with missing required target-synthesis values (none found).
- Dropped after-state controllable parameter columns to avoid leakage.
- Validated `meta_diff_count` against synthesized changed labels.

### Unit 06 - Missing-Value Resolution and Final CSV Validation

- Inspect missing values by column.
- Choose and document an explicit missing-value strategy.
- Ensure the final CSV has no missing values.
- Save exactly one processed CSV:
    - `data/processed/dataset_001.csv`
- Confirm the saved CSV is unsplit and ready for Step 2 EDA.