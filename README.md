# Laser Resonator Beam Alignment Recommendation System

## Project Overview

This project implements an AI recommendation system for laser resonator beam alignment. The goal is to assist a laser operator in transitioning a beam from a current ("before") state to a targeted ("after") state by predicting the necessary adjustments to four controllable alignment parameters:

- **Iris Position**
- **Z Position**
- **Pitch Position**
- **Yaw Position**

Operating as a metadata-only system, it utilizes beam-quality measurements, Gaussian fit percentages, centroids, beam widths, and parsed Gaussian equation parameters to map physical beam shapes to specific hardware adjustments.

## Architectural Approach

The system uses a classical ML, two-stage decoupled architecture to output deterministic, parameter-specific recommendations:

1. **Change Detection**: Four independent classifiers evaluate whether each controllable parameter requires an adjustment.
2. **Delta Regression**: When a parameter is flagged for change, a dedicated regressor predicts the exact adjustment delta (rounded to 2 decimal places). Unchanged parameters default to `0.00`.

## Directory Structure

```text
.
├── data/
│   ├── raw/                 # Place labels.json and sampled_pairs_500k.json here
│   └── processed/           # Transformed datasets (ignored by git)
├── notebooks/               # Jupyter notebooks for EDA and baseline model experimentation
├── scripts/                 # CLI entry points for end-to-end training and evaluation
├── src/                     # Reusable Python modules (data, features, models, evaluation)
└── ai/                      # AI Context, domain logic, and step-by-step implementation trackers
```

## Setup Instructions

This project uses `uv` for lightning-fast Python dependency management.

1. **Install uv**: Follow the instructions on the [uv GitHub page](https://github.com/astral-sh/uv).
2. **Install Dependencies**: Run the following command in the project root to create a `.venv` and install required packages:
    ```bash
    uv sync
    ```
3. **Run Notebooks**: Start Jupyter to explore the initial data prep and EDA stages:
    ```bash
    uv run jupyter notebook
    ```

## Evaluation Strategy

To ensure robust generalizability rather than simple interpolation, models are heavily benchmarked against two distinct splits:

- **Random Split (70/15/15)**: Provides an optimistic baseline.
- **Grouped Split (70/15/15)**: Grouped strictly by `Experiment Number` to serve as extreme validation against unseen physical laser configurations.
