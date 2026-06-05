# Step 1 Outcome: Data Ingestion & Preprocessing

## Final Artifacts

| Artifact          | Path                                         | Status       |
| ----------------- | -------------------------------------------- | ------------ |
| Processed Dataset | `data/processed/dataset_001.csv`             | ✅ Generated |
| Step 1 Notebook   | `notebooks/01_data_ingestion_and_prep.ipynb` | ✅ Executed  |
| Promoted Helpers  | `src/features/gaussian_parser.py`            | ✅ Promoted  |
| Promoted Helpers  | `src/features/targets.py`                    | ✅ Promoted  |
| Promoted Helpers  | `src/data/load_data.py`                      | ✅ Promoted  |

## Dataset Summary

| Metric         | Value    |
| -------------- | -------- |
| Total Rows     | 500,000  |
| Total Columns  | 45       |
| File Size      | 166.1 MB |
| Missing Values | 0        |

## Column Breakdown (45 columns)

### Metadata Columns (5)

- `meta_index1`: Index of before-state record
- `meta_index2`: Index of after-state record
- `meta_diff_count`: Number of controllable parameters changed
- `meta_before_experiment_number`: Before-state experiment identifier
- `meta_after_experiment_number`: After-state experiment identifier

### Before-State Features (18)

- `before_gaussian_fit_percent_along_x`: Gaussian fit percentage along X
- `before_gaussian_fit_percent_along_y`: Gaussian fit percentage along Y
- `before_x_axis_centroid`: X-axis centroid position
- `before_y_axis_centroid`: Y-axis centroid position
- `before_major_axis_beam_width`: Major beam width
- `before_minor_axis_beam_width`: Minor beam width
- `before_effective_diameter`: Effective beam diameter
- `before_ellipticity`: Beam ellipticity
- `before_iris_position`: Iris position (controllable)
- `before_z_position`: Z position (controllable)
- `before_pitch_position`: Pitch position (controllable)
- `before_yaw_position`: Yaw position (controllable)
- `before_power_measurement`: Power measurement
- `before_exposure_time`: Exposure time
- `before_x_gaussian_center_parsed`: Parsed X Gaussian center
- `before_x_gaussian_scale_parsed`: Parsed X Gaussian scale
- `before_y_gaussian_center_parsed`: Parsed Y Gaussian center
- `before_y_gaussian_scale_parsed`: Parsed Y Gaussian scale

### After-State Features (14)

- `after_gaussian_fit_percent_along_x`: Gaussian fit percentage along X
- `after_gaussian_fit_percent_along_y`: Gaussian fit percentage along Y
- `after_x_axis_centroid`: X-axis centroid position
- `after_y_axis_centroid`: Y-axis centroid position
- `after_major_axis_beam_width`: Major beam width
- `after_minor_axis_beam_width`: Minor beam width
- `after_effective_diameter`: Effective beam diameter
- `after_ellipticity`: Beam ellipticity
- `after_power_measurement`: Power measurement
- `after_exposure_time`: Exposure time
- `after_x_gaussian_center_parsed`: Parsed X Gaussian center
- `after_x_gaussian_scale_parsed`: Parsed X Gaussian scale
- `after_y_gaussian_center_parsed`: Parsed Y Gaussian center
- `after_y_gaussian_scale_parsed`: Parsed Y Gaussian scale

### Target Columns (8)

- `target_iris_delta`: Iris position change (3-decimal)
- `target_z_delta`: Z position change (3-decimal)
- `target_pitch_delta`: Pitch position change (3-decimal)
- `target_yaw_delta`: Yaw position change (3-decimal)
- `target_iris_changed`: Binary iris change indicator (0/1)
- `target_z_changed`: Binary Z change indicator (0/1)
- `target_pitch_changed`: Binary pitch change indicator (0/1)
- `target_yaw_changed`: Binary yaw change indicator (0/1)

## Missing-Value Resolution Strategy

### Observation

- Beam quality metrics showed non-random missingness (likely failed Gaussian fitting or corrupted acquisition)
- Before-state beam metrics: 10,092 rows with missing values
- After-state beam metrics: 15,762 rows with missing values

### Resolution Applied

1. **Sentinel Imputation (-1.0)** for beam metrics:
    - `before_gaussian_fit_percent_along_x`: 10,092 NaNs → sentinel
    - `before_gaussian_fit_percent_along_y`: 10,092 NaNs → sentinel
    - `before_effective_diameter`: 10,092 NaNs → sentinel
    - `before_ellipticity`: 10,092 NaNs → sentinel
    - `after_gaussian_fit_percent_along_x`: 15,762 NaNs → sentinel
    - `after_gaussian_fit_percent_along_y`: 15,762 NaNs → sentinel
    - `after_effective_diameter`: 15,762 NaNs → sentinel
    - `after_ellipticity`: 15,762 NaNs → sentinel

2. **Median Imputation** for parsed Gaussian features:
    - All parsed center and scale values imputed with median

3. **Median Imputation** for remaining numeric features:
    - `before_power_measurement`: median
    - `before_exposure_time`: median
    - `after_power_measurement`: median
    - `after_exposure_time`: median

4. **Mode Imputation** for categorical/object features:
    - Experiment number strings: mode value

### Justification

- Sentinel imputation preserves missingness as a learnable signal for tree-based models
- Median imputation is appropriate for mathematically derived features
- Mode imputation is appropriate for categorical features

## Gaussian Parsing Summary

| Axis     | Parse Failures | Success Rate |
| -------- | -------------- | ------------ |
| Before X | 0              | 100%         |
| Before Y | 0              | 100%         |
| After X  | 0              | 100%         |
| After Y  | 0              | 100%         |

All 500,000 pairs parsed successfully with 0 failures.

## Target Synthesis Validation

| Check                                 | Result                     |
| ------------------------------------- | -------------------------- |
| Rows with missing controllable params | 0 (none excluded)          |
| Meta diff count mismatches            | 0                          |
| Target columns created                | 4 deltas + 4 binary labels |

## Validation Results

| Validation                                            | Status  |
| ----------------------------------------------------- | ------- |
| No missing values in final dataset                    | ✅ PASS |
| No raw Gaussian equation string columns               | ✅ PASS |
| No after-state controllable parameter leakage         | ✅ PASS |
| All four before-state controllable parameters present | ✅ PASS |
| All eight target columns present                      | ✅ PASS |
| All required metadata columns present                 | ✅ PASS |
| All changed-label columns are binary 0/1              | ✅ PASS |

## Unresolved Issues

None. Step 1 completed successfully with all validations passing.

## Recommendations for Step 2

1. **EDA Focus Areas**:
    - Analyze beam metric distributions (especially sentinel -1.0 rows)
    - Correlate Gaussian fit percentages with beam quality features
    - Examine target delta distributions by controllable parameter
    - Investigate experiment-based grouping for downstream splitting

2. **Potential Data Slicing**:
    - Evaluate whether grouped splitting by experiment number is appropriate
    - Check for experiment-level shifts in feature distributions

## Notes

- All helper functions validated in the notebook were promoted to `src/` modules for reproducibility
- The 3-decimal target rounding rule (as specified in `ai/context.md`) was applied
- The notebook includes physics-aware imputation that preserves meaningful missingness as a signal
- The final dataset is ready for Step 2 EDA without train/validation/test splitting (per specification)
