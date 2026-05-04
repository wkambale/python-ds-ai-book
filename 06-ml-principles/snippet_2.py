from typing import List, Tuple
import pandas as pd

def prepare_features_and_target(
    df: pd.DataFrame,
    feature_columns: List[str],
    target_column: str
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Separates features and target from a DataFrame.

    Args:
        df: Input DataFrame containing all columns.
        feature_columns: List of column names to use as features.
        target_column: Name of the target column.
    """
    X = df[feature_columns].copy()
    y = df[target_column].copy()
    return X, y

# Define columns
feature_columns = [
    'transaction_count', 
    'avg_transaction_fee', 
    'account_age_days', 
    'support_tickets'
]
target_column = 'churned'

# Separate features and target
X, y = prepare_features_and_target(df_churn, feature_columns, target_column)

print(f"Feature matrix shape: {X.shape}")
print(f"Target vector shape: {y.shape}")
print(f"\nFeature types:\n{X.dtypes}")
print(f"\nTarget distribution:\n{y.value_counts(normalize=True)}")