import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error, r2_score, accuracy_score, 
    precision_score, recall_score, f1_score
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier

def preprocess_data(df, target_col):
    """
    Handles missing values, basic feature selection, and categorical encoding.
    """
    # 1. Drop high-cardinality/ID columns
    cols_to_drop = ['CustomerID', 'TransactionDate', 'PolicyID', 'UnderwrittenCoverID', 'TransactionMonth', 'VehicleModel']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    # 2. Impute missing values
    df = df.fillna(df.median(numeric_only=True))
    df = df.fillna("Unknown")

    # 3. Simple Categorical Encoding (Label Encoding)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category').cat.codes

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 4. Train/Test Split (80:20)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def run_regression_model(model_name, X_train, X_test, y_train, y_test):
    """
    Implements and evaluates Linear Regression, Random Forest, or XGBoost for Regression.
    """
    if model_name == 'lr':
        model = LinearRegression()
    elif model_name == 'rf':
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif model_name == 'xgb':
        model = XGBRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError("Unsupported model name. Use 'lr', 'rf', or 'xgb'.")

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        'RMSE': np.sqrt(mean_squared_error(y_test, preds)),
        'R2': r2_score(y_test, preds)
    }
    return model, metrics

def run_classification_model(model_name, X_train, X_test, y_train, y_test):
    """
    Implements and evaluates Logistic Regression, Random Forest, or XGBoost for Classification.
    """
    if model_name == 'lr':
        model = LogisticRegression(max_iter=1000)
    elif model_name == 'rf':
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_name == 'xgb':
        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    else:
        raise ValueError("Unsupported model name. Use 'lr', 'rf', or 'xgb'.")

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        'Accuracy': accuracy_score(y_test, preds),
        'Precision': precision_score(y_test, preds),
        'Recall': recall_score(y_test, preds),
        'F1': f1_score(y_test, preds)
    }
    return model, metrics