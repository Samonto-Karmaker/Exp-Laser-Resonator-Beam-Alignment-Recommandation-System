# Step 2 Explainer

## Overview

Step 2 is the **Exploratory Data Analysis (EDA)** phase. This step transforms the raw, processed dataset from Step 1 into a fully understood, feature-engineered, and ready-for-modeling state.

This step is **not** about building production models. It's about asking critical questions:

- Do we have enough predictive signal to proceed?
- Which features actually matter?
- How should we encode and transform features for optimal model performance?
- Is grouped splitting by experiment number even appropriate?

## Core Objectives

### 1. Data Quality Assessment

- Detect constant/near-constant features that provide no signal
- Identify potential data leakage (features that inadvertently encode target information)
- Analyze feature distributions and detect outliers
- Validate the sentinel imputation strategy for missing values

### 2. Iterative Benchmark Model Performance Check

- Run quick Random Forest classifiers per parameter (Iris, Z, Pitch, Yaw)
- Calculate average accuracy across all 4 parameters
- **Decision Rule**:
    - If average accuracy < 50%: Stop and flag for further investigation (features may not have predictive signal)
    - If 50% ≤ average accuracy < 70%: Apply feature engineering, re-run benchmark models, repeat up to 2-3 iterations
    - If average accuracy ≥ 70%: Proceed with importance-driven feature engineering
- Stop after 3 iterations if accuracy still < 70%

### 3. Feature Importance Analysis

- Extract feature importances from benchmark models
- Identify top features for each parameter
- Document which features are consistently important vs. parameter-specific

### 4. Encoding & Transformation Strategy

Based on EDA findings, document:

- **Data Encoding**: One-hot, ordinal, or target encoding for categorical features
- **Data Transformations**: Scaling, normalization, log transforms, box-cox
- **Feature Interactions**: Ratios, products, differences for important features
- **Redundancy Cases**: What NOT to do and why (e.g., features already optimized)

### 5. Grouped Split Validity Assessment

- Analyze experiment number distribution across before/after pairs
- Check if experiment numbers create natural groupings that would hurt generalization
- Assess whether grouped splitting (by experiment number) is appropriate for Step 3
- Document the decision: random split vs. grouped split

### 6. Memory Report Generation

Create `ai/memory/eda_insights.md` documenting:

- Key findings from EDA
- Feature engineering strategy with evidence
- Encoding/transformations decision with rationale
- Benchmark model performance summary (including all iteration results)
- Recommendations for Step 3 (data splitting strategy, feature set)

## Expected Deliverables

| Artifact                 | Path                                           | Status           |
| ------------------------ | ---------------------------------------------- | ---------------- |
| EDA Notebook             | `notebooks/02_exploratory_data_analysis.ipynb` | To be created    |
| Memory Report            | `ai/memory/eda_insights.md`                    | To be created    |
| Feature Engineering Plan | Embedded in memory report                      | To be documented |

## Workflow Protocol

1. **Start fresh**: Load `dataset_001.csv` from Step 1
2. **Quality check first**: Don't assume data is ready for modeling
3. **Run benchmark models**: Get quick accuracy signal
4. **Iterate until 70% or 3 attempts**:
    - If accuracy ≥ 70%: proceed with importance-driven engineering
    - If 50% ≤ accuracy < 70%: apply feature engineering, re-run, repeat (max 3 iterations total)
    - If accuracy < 50%: stop and flag for investigation
5. **Document everything**: No decision should be made without evidence
6. **Create memory report**: Capture all insights including all iteration results

## Questions to Answer

By the end of Step 2, we should have clear answers to:

- What is the baseline predictive signal strength?
- Which features should we keep, drop, or engineer?
- How should we encode categorical features?
- Which transformations are necessary?
- Is grouped splitting appropriate, or should we use random splitting?

## Success Criteria

Step 2 is complete when:

1. The EDA notebook has been executed with all analyses
2. The memory report contains clear recommendations for Step 3
3. We have a documented feature engineering strategy
4. We have decided on the data splitting approach for Step 3
5. All key decisions are backed by EDA evidence
