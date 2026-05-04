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
    y_test, y_pred, test_locations, 'Location'