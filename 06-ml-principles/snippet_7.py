from sklearn.linear_model import LogisticRegression

    X_train: np.ndarray,
    y_train: pd.Series,
    random_state: int = 42
) -> LogisticRegression:
    """
    Trains a logistic regression model.

    Args:
        X_train: Scaled training features.