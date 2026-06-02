# AI Context Index

Welcome to the AI Context directory for the **Laser Resonator Beam Alignment** project. This directory acts as the centralized "brain" for the AI coding assistant, holding crucial business logic, step-by-step roadmaps, architectural layouts, and running memory.

## Directory Navigation

Use the links below to access different parts of the project's knowledge base.

- **[context.md](context.md)**: The ultimate source of truth. Contains the primary project overview, domain assumptions, variables, target designs, and business logic.
- **[plan.md](plan.md)**: The strategic high-level roadmap. Outlines the 6 fundamental phases we will follow to achieve the final programmatic recommendation model.
- **[agent.md](agent.md)**: Custom configurations, prompts, and instructions for how the AI agent behaves and processes information on this specific repository.
- **[implementation/PROGRESS.md](implementation/PROGRESS.md)**: The overarching action tracker marking what has been done and what remains.
- **`implementation/step_*_explainer.md`**: Deep-dive strategy documents explaining exact mechanics, expected outputs, and constraints for each of the 6 steps outlined in `plan.md`.
- **`memory/`**: A storage space for logging project-specific insights (like EDA results) and architectural ML decisions.

---

## Proposed File Structure

### Project Repository Structure

A detailed, production-ready experimentation structure to keep data, notebooks, and modular source code organized. Below is the full view including specific file names and their explicit purposes:

```text
.
├── data/
│   ├── raw/                                # Immutable original data
│   │   ├── labels.json                     # Raw beam states and parameter data
│   │   └── sampled_pairs_500k.json         # Raw index pairings mapping before/after transitions
│   └── processed/                          # Transformed datasets (should be git-ignored)
│       ├── dataset_random_split.csv        # The parsed dataset mapped for random splitting
│       └── dataset_grouped_split.csv       # The parsed dataset mapped for experiment-grouped splitting
├── notebooks/                              # Jupyter notebooks for interactive experimentation & visualization
│   ├── 01_data_ingestion_and_prep.ipynb    # Workspace to build and test the data joining & parsing logic
│   ├── 02_exploratory_data_analysis.ipynb  # Visualizations, statistical testing, and bounds analysis
│   └── 03_baseline_model_training.ipynb    # Scratchpad for testing classifier and regressor logic
├── src/                                    # Reusable Python module code (the core ML engine)
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── load_data.py                    # Functions to load large JSONs safely into pandas or dask
│   │   └── make_dataset.py                 # Main orchestrator chaining the raw-to-processed pipeline
│   ├── features/
│   │   ├── __init__.py
│   │   ├── build_features.py               # Joins pairs, handles base feature extraction and absolute values
│   │   ├── gaussian_parser.py              # Regex logic to extract centers/scales from the equation strings
│   │   └── targets.py                      # Logic to calculate 2-decimal parameter deltas and change booleans
│   ├── models/
│   │   ├── __init__.py
│   │   ├── classifiers.py                  # Wrappers for training the 4 parameter-change detection models
│   │   └── regressors.py                   # Wrappers for training the 4 parameter-delta prediction models
│   └── evaluation/
│       ├── __init__.py
│       ├── metrics.py                      # Custom scoring: sign accuracy, tolerance bounds, vector MAE
│       └── splits.py                       # Logic executing random 70/15/15 vs Grouped Split by Experiment ID
├── scripts/                                # Executable CLI entry points to standardize runs
│   ├── train_pipeline.py                   # Script to trigger end-to-end training and save models (.pkl)
│   └── evaluate_models.py                  # Script to run saved models against testing splits and log metrics
├── .gitignore                              # Excludes /data, logs, __pycache__, and compiled model weights
├── requirements.txt                        # Fixed versions for Python libraries (pandas, scikit-learn, xgboost)
└── README.md                               # Developer onboarding, setup instructions, and CLI run commands
```

### AI Context Structure

A dedicated folder to store the rules, context, and memory for the AI coding assistant. An internal `implementation` directory will host the step-by-step explainers and the primary progress tracker:

```text
.
└── ai/
    ├── agent.md                    # Agent configuration and instructions
    ├── context.md                  # Source of truth: assumptions, variables, business logic
    ├── index.md                    # Main entry point indexing the AI context files (this file)
    ├── plan.md                     # Strategic roadmap and high-level steps
    ├── implementation/             # Execution and tracking files
    │   ├── PROGRESS.md             # Comprehensive progress tracker for the entire project
    │   ├── step_01_explainer.md    # Detailed explainer for Step 1 (Data Ingestion)
    │   ├── step_02_explainer.md    # Detailed explainer for Step 2 (EDA)
    │   ├── step_03_explainer.md    # Detailed explainer for Step 3 (Feature Engineering)
    │   ├── step_04_explainer.md    # Detailed explainer for Step 4 (Model Development)
    │   ├── step_05_explainer.md    # Detailed explainer for Step 5 (Evaluation)
    │   └── step_06_explainer.md    # Detailed explainer for Step 6 (Extensions)
    └── memory/                     # Directory to store modular learning from this project
        ├── eda_insights.md         # (Future) Saved conclusions from EDA
        └── architectural_decisions.md # (Future) Logs of why certain ML models were chosen
```
