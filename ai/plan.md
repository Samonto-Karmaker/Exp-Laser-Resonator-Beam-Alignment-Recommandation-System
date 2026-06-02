# Laser Resonator Beam Alignment - Project Plan

## Project Goal

To develop a machine learning-based recommendation system that predicts the precise adjustment amounts (deltas) for four controllable laser tracking parameters (Iris, Z, Pitch, and Yaw positions) required to transition a laser beam from its current ("before") state to a desired ("after") state.

## Inputs

- **`labels.json`**: Contains metadata-only beam state records, including derived measurements (centroids, widths, effective diameter, ellipticity), unparsed Gaussian equation strings, current alignment parameter positions, and system metadata (timestamps, experiment numbers).
- **`sampled_pairs_500k.json`**: Provides 500k index mappings representing "before" and "after" beam states, including a `diff_count` tracking how many controllable parameters changed between the two states.

## Desired Deliverables

1. **Data Pipeline**: A robust preprocessing pipeline that parses strings (like Gaussian equations) into numeric features, joins before/after pairs, and calculates precise target deltas.
2. **EDA Report**: A comprehensive Exploratory Data Analysis summarizing feature relationships, parameter distributions, data boundaries, and validating project assumptions.
3. **Recommendation Model System**: A two-stage classical machine learning inference engine capable of identifying _which_ parameters must change, and _by how much_ they should change.
4. **Validation Framework**: An evaluation suite that measures the model's accuracy on both random distributions and unseen experiments (grouped split).

## Approach Overview

We will tackle this problem using a metadata-only, classical ML approach (Random Forests, Gradient Boosting) as the initial strategy. Rather than attempting a complex end-to-end multi-output deep neural network, we will decompose the problem into a highly interpretable **two-stage per-parameter model**:

1. **Classification Stage**: 4 independent classifiers (one for each parameter) to predict whether a specific parameter needs to change.
2. **Regression Stage**: 4 independent regressors to predict the exact delta (amount and direction) for the parameters flagged by the classifiers.

Outputs and labels will be strictly governed by physical constraints mapped to 2 decimal places to denote valid changes.

---

## Project Steps

### Step 1: Data Ingestion & Target Synthesis

**Overview:** Develop a preprocessing engine to join `labels.json` to `sampled_pairs_500k.json`. Convert raw string data—specifically X and Y Gaussian Equations—into numeric feature columns (centers, scales). Establish the targets by calculating the deltas between the 'after' and 'before' controlled parameters, rounding all deltas to 2 decimal places to create Boolean 'changed' labels and precise numeric values.
**How this leads to the final goal:** Machine learning models require structured, numeric datasets. By converting unparsed equations and abstract indices into clear before/after feature vectors and concrete targets, we build the fundamental ground truth that makes model training possible.

### Step 2: Exploratory Data Analysis (EDA)

**Overview:** Conduct a thorough statistical analysis on the ingested dataset. This includes assessing target balance (classifying how often 0, 1, 2, 3, or 4 parameters change), investigating the predictive value of parsed Gaussian features, and determining whether fields like `Power Measurement` and `Exposure Time` carry useful signals or noise.
**How this leads to the final goal:** EDA prevents "blind modeling." By understanding exact distributions, correlations, and potential data leaks (like time-based drift), we can filter out misleading data and ensure our models learn the true physical relationship between beam shapes and alignments, ensuring a more accurate final recommendation.

### Step 3: Feature Engineering & Strategic Discretization (Data Splitting)

**Overview:** Assemble the final training features comprising standard "before" beam metrics, "before" parameter states, parsed Gaussian features, and the target "after" beam metrics. Following feature selection, partition the data into two strict evaluation splits: an optimistic 70/15/15 random split, and a pragmatic 70/15/15 grouped split strictly segmented by `Experiment Number`.
**How this leads to the final goal:** A model is only as good as its ability to generalize. By structuring the inputs specifically around known "before" variables and desired "after" features, and forcing the model to prove itself on entirely unseen experiments (the grouped split), we guarantee the final product works securely in real-world operating environments, not just memorized lab scenarios.

### Step 4: Two-Stage Model Development

**Overview:** Train the core logic engine using classical ML techniques (e.g., Random Forests, XGBoost). First, train 4 binary classifiers to detect whether Iris, Z, Pitch, or Yaw require adjustment. Next, train 4 regressors exclusively on the subsets of data where those parameters actually changed to predict the physical delta required.
**How this leads to the final goal:** This step is the creation of the recommendation brain itself. The two-stage architecture directly mimics the operator's decision process (deciding _what_ to touch, then deciding _how much_ to turn it). Keeping parameters isolated allows us to pinpoint and debug performance issues at the per-parameter level, guaranteeing the final deliverable is accurate and trustworthy.

### Step 5: End-to-End Evaluation & Synthesis

**Overview:** Connect the classification and regression models into a single inference pipeline. Evaluate the model end-to-end to see if it correctly predicts 0.00 for unchanged parameters and accurate deltas for changed ones. Benchmark using metrics like vector Mean Absolute Error (MAE), sign direction accuracy, and change-count accuracy (validated against `diff_count`).
**How this leads to the final goal:** Generating predictions is useless if they can't be trusted. This step translates raw mathematical error metrics into practical hardware realities (e.g., "Is the predicted pitch within a 0.05 tolerance?"). Validating the end-to-end vector ensures the final recommendations served to operators are safe, resulting in the successful automated alignment of the laser resonator.

### Step 6: Future Extensions & Refinements (Post-V1)

**Overview:** Plan architecture integrations for downstream capabilities, such as incorporating raw beam imagery for hybrid modeling (image + metadata), adding physical parameter clipping constraints, mapping numeric outputs to human-readable UI instructions, or attempting a multi-output model to capture cross-parameter coupling.
**How this leads to the final goal:** Ensures the system architecture remains scalable, accommodating more complex intelligence and better operator interfaces as project maturity grows.
