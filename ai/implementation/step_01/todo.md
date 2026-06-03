# Step 1 Todo: Data Ingestion & Preprocessing

This checklist is grouped into execution units that can move through the sprint flow together. Units are ordered by dependency, but each unit has a clear review boundary and artifact expectation.

## Backlog

### Unit 03 - Pair Join and Role-Based Column Layout

- Join before/after states using `index1` and `index2`.
- Rename columns with role prefixes: `before_`, `after_`, `target_`, and `meta_`.
- Keep required metadata columns:
  - `meta_index1`
  - `meta_index2`
  - `meta_before_experiment_number`
  - `meta_after_experiment_number`
  - `meta_diff_count`
- Keep before-state controllable parameter columns as model input features.
- Drop direct date/time/file metadata from the final CSV:
  - `Date`
  - `Timestamp`
  - `filename`

### Unit 04 - Gaussian Parsing and Raw String Cleanup

- Parse before/after X/Y Gaussian equation strings into numeric center and scale fields.
- Report Gaussian parse failure counts.
- Inspect parse failure examples or patterns before choosing cleanup behavior.
- Drop raw Gaussian equation string columns after parsing.

### Unit 05 - Target Synthesis and Leakage Checks

- Compute the four target delta columns using raw numeric values and standard Python/pandas 2-decimal rounding.
- Compute the four binary changed-label columns.
- Exclude rows with missing required target-synthesis values; never impute targets.
- Drop after-state controllable parameter columns after target synthesis.
- Validate `meta_diff_count` against synthesized changed labels and report warnings if mismatches exist.

### Unit 06 - Missing-Value Resolution and Final CSV Validation

- Inspect missing values by column.
- Choose and document an explicit missing-value strategy.
- Ensure the final CSV has no missing values.
- Save exactly one processed CSV:
  - `data/processed/dataset_001.csv`
- Confirm the saved CSV is unsplit and ready for Step 2 EDA.

### Unit 07 - End-of-Step Review and Promotion Decision

- Review whether any validated helper logic should be promoted into `src/`.
- Record the Step 1 outcome, generated artifact, validation summary, and any unresolved issues in `ai/implementation/step_01/outcome.md`.
- Prepare Step 1 for completion by clearing granular tasks from `ai/implementation/PROGRESS.md` and adding the final step summary when all units are done.

## To Do

### Unit 02 - Raw Data Loading and Schema Validation

- Confirm expected raw data paths:
  - `data/raw/labels.json`
  - `data/raw/sampled_pairs_500k.json`
- Write and run Python code in the Step 1 notebook to load both raw files.
- Inspect shapes, sample records, field names, and basic schema characteristics through notebook/Python output.
- Validate required fields for pair joining, beam features, Gaussian parsing, target synthesis, and metadata retention through notebook/Python code.
- Document any schema assumptions or unexpected raw-field issues in the notebook.
- Do not rely on model-side/manual inspection of raw JSON files as the source of truth for Unit 02.

## In Progress

-

## In Review

-

## Done

### Unit 01 - Notebook Scaffold and Run Context

- Created `notebooks/01_data_ingestion_and_prep.ipynb`.
- Defined project-root-relative paths in the notebook.
- Added a notebook structure matching the Step 1 flow: load, validate, join, parse, synthesize targets, resolve missing values, validate output, save CSV.
- Verified the notebook JSON parses successfully.
