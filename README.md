# Insurance Risk Analytics - Predictive Modeling

## Project Overview

This project focuses on exploratory data analysis (EDA) and risk assessment within an insurance portfolio dataset. The analysis aims to uncover profitability patterns, claim behavior, customer risk characteristics, and geographic trends that influence insurance performance.

The project emphasizes:

* reproducible analytics workflows
* modular Python development
* data quality assessment
* risk and profitability analysis
* professional visualization and reporting practices

---

# Project Objectives

The main objectives of this project are:

* Perform comprehensive exploratory data analysis (EDA)
* Assess portfolio profitability using Loss Ratio analysis
* Identify trends in claims, premiums, and customer behavior
* Detect outliers and anomalies in financial variables
* Analyze geographic and temporal risk patterns
* Build reusable and maintainable analytics modules
* Establish a reproducible development workflow using GitHub Actions CI

---

# Project Structure

```text
insurance-risk-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── MachineLearningRating_v3.txt
│
├── notebooks/
│   └── 01-eda.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   └── visualization.py
│
├── tests/
│   └── test_loader.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Exploratory Data Analysis Coverage

The analysis includes:

## Data Summarization

* Descriptive statistics
* Data type validation
* Numerical and categorical feature inspection

## Data Quality Assessment

* Missing value analysis
* Missing value handling strategy
* Data consistency checks

## Univariate Analysis

* Histograms
* Distribution analysis
* Bar charts for categorical variables

## Bivariate & Multivariate Analysis

* Correlation analysis
* Scatter plots
* Premium vs claims relationship analysis

## Geographic Trends

* Province-level premium and claims analysis
* Vehicle and cover type comparisons

## Outlier Detection

* Box plots
* Extreme value analysis
* Financial anomaly inspection

## Temporal Trend Analysis

* Monthly claims trends
* Claim severity evolution
* Time-based profitability patterns

---

# Key Analytical Questions

This project addresses the following business questions:

* What is the overall portfolio Loss Ratio?
* How does Loss Ratio vary across Province, VehicleType, and Gender?
* Which financial variables contain significant outliers?
* Are there temporal trends in claim frequency or severity?
* Which vehicle makes/models generate the highest claims?
* Which customer segments demonstrate elevated underwriting risk?

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Git & GitHub
* GitHub Actions CI

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
```

## 2. Navigate into Project

```bash
cd insurance-risk-analytics
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How to Run the Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebooks/01-eda.ipynb
```

Run all notebook cells sequentially for full analysis reproduction.

---

# Continuous Integration (CI)

The project includes a GitHub Actions CI pipeline that automatically:

* installs dependencies
* runs linting checks
* executes tests on every push

This ensures code quality and reproducibility across environments.

## DVC Pipeline Reproducibility

### Initialize Environment
```bash
pip install -r requirements.txt
```

### Initialize DVC
```bash
dvc init
```

### Pull Data
```bash
dvc pull
```

### Reproduce Data Pipeline
Raw and cleaned datasets are tracked using DVC with local remote storage.

---

# Author

Bethelhem F.H
