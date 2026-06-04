# Implementation Progress Board

## Navigation & Agent Guide

This board manages the project state using a Jira-like sprint flow, focusing on **one step at a time**.

- **Sprint Flow**: We divide each step into actionable sub-tasks and manage them through `Backlog` -> `To Do` -> `In Progress` -> `In Review` -> `Done`.
- **Step Folder Sync**: The active step's detailed todo list must be maintained in `ai/implementation/step_##/todo.md`. Its scope and rules live in `explainer.md`, and its completion summary lives in `outcome.md`.
- **Completion Protocol**: Once an entire step is complete, all of its granular sub-tasks are cleared from this board. In the `Done` section, we only leave the **Step Name**, a **short description** of what was achieved, and links to the step folder files.

> **Context Optimization Rule (For AI Agent):**
> Do **NOT** read historical step folders linked in the "Done" section by default. Only read historical step files if you explicitly identify a dependency or require specific context to complete the task in-hand. Read nothing more, nothing less.

## Backlog

_(Sub-tasks for future steps or overflow from the current step)_

### Step 1 / Unit 07 - End-of-Step Review and Promotion Decision

- Decide whether any validated notebook helper logic should be promoted into `src/`.
- Update `ai/implementation/step_01/outcome.md` with artifacts, validations, and unresolved issues.
- When Step 1 is fully complete, clear granular Step 1 tasks from this board and add a single Step 1 summary entry under Done.

## To Do

_(Actionable sub-tasks for the current step)_

## In Progress

## In Review

_(Sub-tasks that are executed but pending verification/evaluation)_

## Done

_(Completed steps. Link to step folder files here. Clear out granular sub-tasks once the whole step is done.)_

### Step 1 / Unit 01 - Notebook Scaffold and Run Context

- Created `notebooks/01_data_ingestion_and_prep.ipynb`.
- Defined project-root-relative paths in the notebook.
- Added notebook sections for load, validate, join, parse, synthesize targets, resolve missing values, validate output, and save CSV.
- Verified the notebook JSON parses successfully.

### Step 1 / Unit 02 - Raw Data Loading and Schema Validation

- Confirm raw paths for `labels.json` and `sampled_pairs_500k.json`.
- Write and run Python code in the Step 1 notebook to load the raw files.
- Inspect shapes, sample records, field names, and basic schema characteristics through notebook/Python output.
- Validate fields required for pair joining, candidate features, Gaussian parsing, targets, and metadata retention through notebook/Python code.
- Document schema assumptions or unexpected raw-field issues in the Step 1 notebook.
- Do not rely on model-side/manual inspection of raw JSON files as the source of truth for Unit 02.

### Step 1 / Unit 03 - Pair Join and Role-Based Column Layout

- Joined before/after states using `index1` and `index2`.
- Formatted columns with `before_`, `after_`, and `meta_` prefix roles.
- Retained required grouping metadata (`meta_index1`, `meta_index2`, `meta_diff_count`, `meta_before_experiment_number`, `meta_after_experiment_number`) and before-state controllable parameters.
- Dropped direct date, timestamp, and filename columns from the dataset.

### Step 1 / Unit 04 - Gaussian Parsing and Raw String Cleanup

- Parse before/after X/Y Gaussian equations into numeric center and scale features.
- Reported 0 parse failures across all 500,000 pairs (all parsed successfully).
- Dropped raw Gaussian equation string columns from the final joined dataset.

### Step 1 / Unit 05 - Target Synthesis and Leakage Checks

- Computed the four target delta columns using raw numeric values and standard Python/pandas 3-decimal rounding.
- Computed the four binary changed-label columns.
- Excluded rows with missing required target-synthesis values (none found).
- Dropped after-state controllable parameter columns to avoid leakage.
- Validated `meta_diff_count` against synthesized changed labels.

### Step 1 / Unit 06 - Missing-Value Resolution and Final CSV Validation

- Inspect missing values by column.
- Choose and document the missing-value strategy.
- Verify the final dataset has no missing values.
- Save exactly one unsplit processed CSV to `data/processed/dataset_001.csv`.
