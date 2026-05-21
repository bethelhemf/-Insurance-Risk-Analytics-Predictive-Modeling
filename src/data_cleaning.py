"""
data_cleaning.py

Contains reusable data quality assessment functions.
"""

import pandas as pd


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate missing value summary report.
    """

    missing_count = df.isnull().sum()

    missing_percent = (missing_count / len(df)) * 100

    report = pd.DataFrame({
        "Missing Values": missing_count,
        "Percentage": missing_percent
    })

    return report.sort_values(
        by="Percentage",
        ascending=False
    )


def convert_date(df: pd.DataFrame, column: str):
    """
    Convert date column into datetime format.
    """

    df[column] = pd.to_datetime(df[column])

    return df