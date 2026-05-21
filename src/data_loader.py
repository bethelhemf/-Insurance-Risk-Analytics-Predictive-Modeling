"""
data_loader.py

Handles dataset loading functionality.
Supports loading structured TXT insurance datasets.
"""

import pandas as pd


def load_data(file_path: str, separator: str = "|") -> pd.DataFrame:
    """
    Load insurance dataset.

    Parameters
    ----------
    file_path : str
        Path to dataset.

    separator : str
        Delimiter used in TXT file.

    Returns
    -------
    pd.DataFrame
        Loaded dataframe.
    """

    try:
        df = pd.read_csv(file_path, sep=separator)

        print(f"Dataset loaded successfully: {df.shape}")

        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")