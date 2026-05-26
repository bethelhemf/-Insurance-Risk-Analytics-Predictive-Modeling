import pandas as pd
from scipy import stats

def perform_chi_square_test(df, group_col, target_col):
    """Used for categorical KPIs like Claim Frequency."""
    contingency_table = pd.crosstab(df[group_col], df[target_col])
    chi2, p, dof, ex = stats.chi2_contingency(contingency_table)
    return chi2, p

def perform_t_test(group_a, group_b):
    """Used for numerical KPIs like Claim Severity or Margin."""
    # Ensure no NaN values for the test
    group_a = group_a.dropna()
    group_b = group_b.dropna()
    t_stat, p_value = stats.ttest_ind(group_a, group_b, nan_policy='omit')
    return t_stat, p_value

def calculate_metrics(df):
    """Adds KPI columns to the dataframe."""
    df['HasClaim'] = df['TotalClaims'] > 0
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df