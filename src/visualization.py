"""
visualization.py

Visualization utility functions.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def histogram_plot(df, column):
    """
    Plot histogram for numerical variables.
    """

    plt.figure(figsize=(10, 5))

    sns.histplot(df[column], kde=True)

    plt.title(f"Distribution of {column}")

    plt.xlabel(column)

    plt.ylabel("Frequency")

    plt.show()


def boxplot_plot(df, column):
    """
    Detect outliers using boxplot.
    """

    plt.figure(figsize=(10, 4))

    sns.boxplot(x=df[column])

    plt.title(f"Boxplot of {column}")

    plt.show()


def correlation_heatmap(df, numeric_columns):
    """
    Plot correlation matrix.
    """

    plt.figure(figsize=(12, 8))

    correlation = df[numeric_columns].corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Matrix")

    plt.show()