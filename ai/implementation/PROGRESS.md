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

## To Do

_(Actionable sub-tasks for the current step, grouped into independent units)_

### Unit 01: Data Quality Assessment

1. Load `dataset_001.csv` and perform initial data quality assessment
2. Check for constant/near-constant features
3. Check for potential data leakage (features with extreme correlation to targets)
4. Analyze feature distributions and detect outliers

### Unit 02: Benchmark Model Iteration (0-3 attempts)

5. Run benchmark Random Forest models for all 4 parameters (Iris, Z, Pitch, Yaw)
6. Calculate average accuracy and determine next steps
7. **Iterative Process** (repeat up to 3 times if accuracy < 70%):
    - If accuracy ≥ 70%: Extract feature importances for each parameter
    - If 50% ≤ accuracy < 70%: Apply feature engineering, re-run benchmark models, repeat
    - If accuracy < 50%: Stop and flag for investigation

### Unit 03: Feature Engineering Strategy

8. Document encoding strategies (one-hot, ordinal, target)
9. Document transformation strategies (scaling, normalization, log transforms)
10. Document feature engineering recommendations matrix
11. Document redundancy cases (what NOT to do and why)

### Unit 04: Split Strategy Assessment

12. Analyze experiment number distribution for grouped split validity

### Unit 05: Documentation & Sign-off

13. Create `ai/memory/eda_insights.md` report with all findings
14. Update `ai/implementation/step_02/outcome.md` with summary
15. **Promote reusable EDA functions to `src/`** (e.g., quality check functions, encoding helpers, transformation utilities)

## In Progress

## In Review

_(Sub-tasks that are executed but pending verification/evaluation)_

## Done

_(Completed steps. Link to step folder files here. Clear out granular sub-tasks once the whole step is done.)_

### Step 1 / Data Ingestion & Preprocessing

- Completed notebook scaffold and raw data loading (Units 01-02)
- Joined before/after states with role-based column prefixes (Unit 03)
- Parsed Gaussian equations (0 failures, promoted to `src/features/gaussian_parser.py`) (Unit 04)
- Synthesized targets and validated against meta_diff_count (Unit 05)
- Resolved missing values with sentinel/median imputation, saved `dataset_001.csv` (Unit 06)
- Promoted validated helper logic to `src/` modules (Units 07)

See [`ai/implementation/step_01/outcome.md`](step_01/outcome.md) for full details.
