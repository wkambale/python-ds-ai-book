import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_logistic_regression(
    X_train: np.ndarray,
    y_train: pd.Series,
    random_state: int = 42
) -> LogisticRegression:
    """
    Trains a logistic regression model.

    Args:
        X_train: Scaled training features.
        y_train: Target labels.
        random_state: Random state for reproducibility.

    Returns:
        Fitted LogisticRegression model.
    """
    model = LogisticRegression(random_state=random_state)
    model.fit(X_train, y_train)
    return model