# Prediction of Disease Type Based on Underlying Mechanisms: Gene Expression versus Post-Transcriptional Drivers 

The **MLForScientists** repository features structured workflows for classification and dimensionality reduction using real-world datasets from cancer research and neuroscience.

## Objective
Using supervised learning algorithms, we examine whether disease type can be more accurately predicted from single-cell RNA-sequencing (scRNA-seq) data in transcriptionally driven diseases like cancer versus in post-transcriptionally driven diseases like dementia. 

## Project Structure

```
MLForScientists
│
├── env.yaml                            # Conda environment specification
├── README.md                           # Project description
├── data/
│   ├── cancer_dataset.csv              # Combined cancer dataset
│   ├── neuro_dataset.csv               # Combined neuroscience dataset
│   ├── train_cancer.csv                # Training data for cancer
│   ├── test_cancer.csv                 # Test data for cancer
│   ├── train_neuro.csv                 # Training data for neuroscience
│   └── test_neuro.csv                  # Test data for neuroscience
│
└── models/
    ├── KNN_Neuro_And_Cancer.ipynb      # KNN classification for both datasets
    ├── PCA_Cancer.ipynb                # PCA analysis on cancer data
    ├── PCA_Neuro.ipynb                 # PCA analysis on neuroscience data
    ├── SoftMax_Cancer.ipynb            # SoftMax classifier on cancer data
    ├── SoftMax_Neuro.ipynb             # SoftMax classifier on neuroscience data
    ├── preprocess_dataset.ipynb        # Preprocessing for both cancer/neuroscience
    ├── xgboost_model_cancer_dataset.ipynb  # XGBoost on cancer data
    └── xgboost_model_neuro_dataset.ipynb   # XGBoost on neuroscience data
```

## Setup

To set up your environment:

```bash
conda env create -f env.yaml
conda activate MLForScientists
```

Ensure Jupyter is installed in your environment to run the notebooks:

```bash
conda install notebook
```

## Features

- **Dimensionality Reduction**: PCA is used to explore and reduce feature space complexity.
- **Classification Models**:
  - **K-Nearest Neighbors (KNN)** for simple, interpretable classification.
  - **SoftMax Regression** for probabilistic multi-class classification.
  - **XGBoost** for powerful gradient-boosted decision tree models.
- **Data Handling**: Cleanly separated training and testing data for model validation.

## Datasets

- **Cancer and Neuroscience datasets** are stored as CSV files.
- Datasets include pre-split training and testing files to facilitate direct model training and evaluation.

## Usage

Each notebook is self-contained and can be run independently. Open the `.ipynb` files in Jupyter Notebook or JupyterLab to explore data preprocessing, model training, and results visualization.

