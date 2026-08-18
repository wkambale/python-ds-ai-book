import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def check_fairness_by_group(
    y_true: pd.Series,
    y_pred: np.ndarray,
    sensitive_feature: pd.Series,
    feature_name: str
) -> pd.DataFrame:
    """
    Checks model performance across groups defined by a sensitive feature.

    Args:
        y_true: Actual labels.
        y_pred: Predicted labels.
        sensitive_feature: Feature to group by.
        feature_name: Name of the feature for display.
    """
    results = []
    df = pd.DataFrame({'true': y_true, 'pred': y_pred, 'group': sensitive_feature})
    for group, group_df in df.groupby('group'):
        results.append({
            feature_name: group,
            'Count': len(group_df),
            'Accuracy': accuracy_score(group_df['true'], group_df['pred']),
            'Precision': precision_score(group_df['true'], group_df['pred'], zero_division=0),
            'Recall': recall_score(group_df['true'], group_df['pred'], zero_division=0),
            'F1': f1_score(group_df['true'], group_df['pred'], zero_division=0)
        })
    return pd.DataFrame(results)