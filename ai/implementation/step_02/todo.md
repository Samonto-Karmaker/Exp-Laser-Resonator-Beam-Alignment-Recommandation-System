# Step 2 Todo

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

_(Sub-tasks currently being worked on)_

## In Review

_(Sub-tasks that are executed but pending verification/evaluation)_

## Done

_(Completed tasks - leave empty until Step 2 is fully complete)_
