# Implementation Progress Board

## Navigation & Agent Guide

This board manages the project state using a Jira-like sprint flow, focusing on **one step at a time**.

- **Sprint Flow**: We divide each step into actionable sub-tasks and manage them through `Backlog` -> `To Do` -> `In Progress` -> `In Review` -> `Done`.
- **Step Folder Sync**: The active step's detailed todo list must be maintained in `ai/implementation/step_##/todo.md`. Its scope and rules live in `explainer.md`, and its completion summary lives in `outcome.md`.
- **Completion Protocol**: Once an entire step is complete, all of its granular sub-tasks are cleared from this board. In the "Done" section, we only leave the **Step Name**, a **short description** of what was achieved, and links to the step folder files.

> **Context Optimization Rule (For AI Agent):**
> Do **NOT** read historical step folders linked in the "Done" section by default. Only read historical step files if you explicitly identify a dependency or require specific context to complete the task in-hand. Read nothing more, nothing less.

## Backlog

_(Sub-tasks for future steps or overflow from the current step)_

## To Do

_(Actionable sub-tasks for the current step, grouped into independent units)_

### Unit 02: Benchmark Model Iteration (0-3 attempts)

7. Run benchmark Random Forest models for all 4 parameters (Iris, Z, Pitch, Yaw)
8. Calculate average accuracy and determine next steps
9. **Iterative Process** (repeat up to 3 times if accuracy < 70%):
    - If accuracy ≥ 70%: Extract feature importances for each parameter
    - If 50% ≤ accuracy < 70%: Apply feature engineering, re-run benchmark models, repeat
    - If accuracy < 50%: Stop and flag for investigation
10. **Visualize**: Create bar plot of feature importances for each parameter
11. **Visualize**: Create accuracy comparison plot across iterations

### Unit 03: Feature Engineering Strategy

12. Document encoding strategies (one-hot, ordinal, target)
13. Document transformation strategies (scaling, normalization, log transforms)
14. Document feature engineering recommendations matrix
15. Document redundancy cases (what NOT to do and why)
16. **Visualize**: Create before/after comparison plots for engineered features (if applicable)

### Unit 04: Split Strategy Assessment

17. Analyze experiment number distribution for grouped split validity
18. **Visualize**: Create histogram of experiment numbers (before/after)
19. **Visualize**: Create overlap analysis plot showing experiment distribution

### Unit 05: Documentation & Sign-off

20. Create `ai/memory/eda_insights.md` report with all findings
21. Update `ai/implementation/step_02/outcome.md` with summary
22. **Promote reusable EDA functions to `src/`** (e.g., quality check functions, encoding helpers, transformation utilities)
23. **Visualize**: Create final summary dashboard showing all key findings

### Unit 06: Model-Ready Dataset

24. Apply encoding transformations to categorical features (one-hot, ordinal, or target encoding)
25. Apply numeric transformations (scaling, normalization, log transforms) as needed
26. Remove constant/near-constant features
27. Remove features with data leakage
28. Save final dataset as `data/processed/dataset_002.csv`
29. **Visualize**: Create final dataset overview (column count, row count, feature types)

## In Progress

## In Review

_(Sub-tasks that are executed but pending verification/evaluation)_

## Done

_(Completed tasks for this step)_

### Unit 01: Data Quality Assessment ✅

**Completed:** All 6 tasks

1. ✅ Loaded `dataset_001.csv` and performed initial data quality assessment (500K rows × 45 columns, 0 missing values)
2. ✅ Checked for constant/near-constant features (2 constant features identified: `before_exposure_time`, `after_exposure_time`)
3. ✅ Checked for potential data leakage (PASSED - no features with |r| ≥ 0.80 to targets)
4. ✅ Analyzed feature distributions and detected outliers (IQR method, 9-20% outliers in various features)
5. ✅ Created distribution plots for key features (controllable parameters, beam metrics, targets)
6. ✅ Created correlation heatmap for features vs targets (top 20 features by variance)

**Key Findings:**

- No missing values (sentinel imputation successful)
- No data leakage detected
- 2 constant features removed: `before_exposure_time`, `after_exposure_time`
- Dataset reduced from 45 to 43 columns
- Class imbalance detected: Pitch (90.55% changed), Yaw (90.28% changed)
- Before parameter positions are strongest predictors (r ≈ 0.7 with deltas)

**Status:** Complete and approved

---

_(Once entire Step 2 is complete, all unit details above will be consolidated into a single Step 2 summary)_

### Step 1 / Data Ingestion & Preprocessing

- Completed notebook scaffold and raw data loading (Units 01-02)
- Joined before/after states with role-based column prefixes (Unit 03)
- Parsed Gaussian equations (0 failures, promoted to `src/features/gaussian_parser.py`) (Unit 04)
- Synthesized targets and validated against meta_diff_count (Unit 05)
- Resolved missing values with sentinel/median imputation, saved `dataset_001.csv` (Unit 06)
- Promoted validated helper logic to `src/` modules (Units 07)

See [`ai/implementation/step_01/outcome.md`](step_01/outcome.md) for full details.
