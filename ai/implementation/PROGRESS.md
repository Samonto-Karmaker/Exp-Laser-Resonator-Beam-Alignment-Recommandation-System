# Implementation Progress Board

## Navigation & Agent Guide

This board manages the project state using a Jira-like sprint flow, focusing on **one step at a time**.

- **Sprint Flow**: We divide each step into actionable sub-tasks and manage them through `Backlog` -> `To Do` -> `In Progress` -> `In Review` -> `Done`.
- **Step Folder Sync**: The active step's detailed todo list must be maintained in `ai/implementation/step_##/todo.md`. Its scope and rules live in `explainer.md`, and its completion summary lives in `outcome.md`.
- **Completion Protocol**: Once an entire step is complete, all of its granular sub-tasks are cleared from this board. In the `Done` section, we only leave the **Step Name**, a **short description** of what was achieved, and links to the step folder files.

> **Context Optimization Rule (For AI Agent):**
> Do **NOT** read historical step folders linked in the "Done" section by default. Only read historical step files if you explicitly identify a dependency or require specific context to complete the task in-hand. Read nothing more, nothing less.

---

## Backlog

*(Sub-tasks for future steps or overflow from the current step)*

### Step 1 / Unit 03 - Pair Join and Role-Based Column Layout

- Join before/after states using `index1` and `index2`.
- Apply `before_`, `after_`, `target_`, and `meta_` column roles.
- Retain required audit/grouping metadata and before-state controllable parameters.
- Drop direct date/time/file metadata from the final CSV.

### Step 1 / Unit 04 - Gaussian Parsing and Raw String Cleanup

- Parse before/after X/Y Gaussian equations into numeric center and scale features.
- Report parse failure counts and inspect failure patterns.
- Drop raw Gaussian equation strings after parsing.

### Step 1 / Unit 05 - Target Synthesis and Leakage Checks

- Build 2-decimal target deltas and numeric binary changed labels.
- Exclude rows missing required target-synthesis values; never impute targets.
- Drop after-state controllable parameter columns after target synthesis.
- Validate synthesized changed-label counts against `meta_diff_count`.

### Step 1 / Unit 06 - Missing-Value Resolution and Final CSV Validation

- Inspect missing values by column.
- Choose and document the missing-value strategy.
- Verify the final dataset has no missing values.
- Save exactly one unsplit processed CSV to `data/processed/dataset_001.csv`.

### Step 1 / Unit 07 - End-of-Step Review and Promotion Decision

- Decide whether any validated notebook helper logic should be promoted into `src/`.
- Update `ai/implementation/step_01/outcome.md` with artifacts, validations, and unresolved issues.
- When Step 1 is fully complete, clear granular Step 1 tasks from this board and add a single Step 1 summary entry under Done.

## To Do

*(Actionable sub-tasks for the current step)*

### Step 1 / Unit 02 - Raw Data Loading and Schema Validation

- Confirm raw paths for `labels.json` and `sampled_pairs_500k.json`.
- Load raw files; inspect shapes and sample records.
- Validate fields required for pair joining, candidate features, Gaussian parsing, targets, and metadata retention.
- Document schema assumptions or unexpected raw-field issues in the Step 1 notebook.

## In Progress

*(What is actively being worked on right now)*

-

## In Review

*(Sub-tasks that are executed but pending verification/evaluation)*

-

## Done

*(Completed steps. Link to step folder files here. Clear out granular sub-tasks once the whole step is done.)*

### Step 1 / Unit 01 - Notebook Scaffold and Run Context

- Created `notebooks/01_data_ingestion_and_prep.ipynb`.
- Defined project-root-relative paths in the notebook.
- Added notebook sections for load, validate, join, parse, synthesize targets, resolve missing values, validate output, and save CSV.
- Verified the notebook JSON parses successfully.
