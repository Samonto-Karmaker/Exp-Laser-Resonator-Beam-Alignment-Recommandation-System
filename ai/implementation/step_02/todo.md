# Step 2 Todo

## Backlog

_(Sub-tasks for future steps or overflow from the current step)_

## To Do

_(Actionable sub-tasks for the current step, grouped into independent units)_

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

_(Sub-tasks currently being worked on)_

## In Review

_(Sub-tasks that are executed but pending verification/evaluation)_

## Done

_(Completed tasks - will be consolidated at end of Step 2)_

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

### Unit 02: Benchmark Models - Complete (Classification + Regression)

**Classification Benchmarks:** 7. ✅ Run benchmark Random Forest classifiers for all 4 parameters (Iris, Z, Pitch, Yaw) 8. ✅ Calculate average accuracy: **98.91%** (far exceeds 70% threshold) 9. ✅ Extract feature importances for each parameter

**Regression Benchmarks:** 10. ✅ Run benchmark Random Forest regressors for all 4 parameter deltas 11. ✅ Calculate MAE, RMSE, R², sign accuracy 12. ✅ All regression benchmarks PASSED success criteria

**Visualizations:** 13. ✅ Classification: Top features, cumulative importance, heatmap, category analysis 14. ✅ Regression: Predicted vs actual, residuals, MAE/R² comparison 15. ✅ Regression feature importance: Top features extraction and classification vs regression comparison

**Key Insight from Feature Comparison:**

- `before_parameter_position` DOMINATES regression (30-50% importance) but is less dominant in classification (14-20%)
- Regression is simpler: Top 20 features = 99.97% cumulative importance
- Classification is more complex: Top 20 features = 89-95% cumulative importance
- **Validates two-stage architecture**: Stages solve fundamentally different sub-problems (effect-based vs cause-based)

**Results Summary:**

**Classification:**

- Average Test Accuracy: **98.91%**
- Iris: 99.36%, Z: 99.99%, Pitch: 98.44%, Yaw: 97.85%

**Regression:**

- Average Test R²: **0.9993** (99.93% variance explained)
- Average Sign Accuracy: **98.59%**
- Average Normalized MAE: **0.05%** of delta range
- Iris MAE: 2.46 (✅ < 100), Z MAE: 0.0071 (✅ < 2)
- Pitch MAE: 0.0002 (✅ < 0.02), Yaw MAE: 0.0002 (✅ < 0.02)

**Decision:**

- ✅ Two-stage architecture is VALIDATED
- ✅ Feature set is SUFFICIENT (no engineering needed)
- ✅ Skip Units 03 (feature engineering)

**Status:** Complete and approved

### Unit 03: Feature Engineering Strategy - Skipped

12. Document encoding strategies (one-hot, ordinal, target)
13. Document transformation strategies (scaling, normalization, log transforms)
14. Document feature engineering recommendations matrix
15. Document redundancy cases (what NOT to do and why)
16. **Visualize**: Create before/after comparison plots for engineered features (if applicable)
