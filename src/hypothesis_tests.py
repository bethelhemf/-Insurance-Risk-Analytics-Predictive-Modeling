import pandas as pd
from scipy import stats

def perform_chi_square_test(df, group_col, target_col):
    """Used for categorical KPIs like Claim Frequency."""
    # Ensure we don't have empty data
    if df.empty:
        return None, 1.0
    contingency_table = pd.crosstab(df[group_col], df[target_col])
    if contingency_table.empty:
        return None, 1.0
    chi2, p, dof, ex = stats.chi2_contingency(contingency_table)
    return chi2, p

def perform_t_test(group_a, group_b):
    """Used for numerical KPIs like Claim Severity or Margin."""
    group_a = group_a.dropna()
    group_b = group_b.dropna()
    if len(group_a) < 2 or len(group_b) < 2:
        return None, 1.0
    t_stat, p_value = stats.ttest_ind(group_a, group_b, nan_policy='omit')
    return t_stat, p_value

def calculate_metrics(df):
    """Adds KPI columns to the dataframe."""
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df