"""
eda_analysis.py

Reusable exploratory data analysis functions.
"""

import pandas as pd


def descriptive_statistics(df: pd.DataFrame):
    """
    Display descriptive statistics for numerical variables.
    """

    return df.describe()


def categorical_summary(df: pd.DataFrame):
    """
    Display categorical variable information.
    """

    return df.select_dtypes(include='object').describe()


def calculate_loss_ratio(df: pd.DataFrame):
    """
    Compute portfolio loss ratio.
    """

    total_claims = df['TotalClaims'].sum()

    total_premium = df['TotalPremium'].sum()

    loss_ratio = total_claims / total_premium

    return round(loss_ratio, 4)