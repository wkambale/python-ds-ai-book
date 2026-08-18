import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score

def evaluate_cross_validation(
    model,
    X: np.ndarray,
    y: pd.Series,
    cv: int = 5,
    scoring: str = 'f1'
) -> np.ndarray:
    """
    Performs k-fold cross-validation and reports results.

    Args:
        model: Scikit-learn model (will be cloned for each fold).
        X: Feature matrix.
        y: Target vector.
        cv: Number of folds.
        scoring: Metric to evaluate.
    """
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    print(f"Cross-Validation ({cv}-Fold) {scoring.upper()} Scores: {scores}")
    print(f"Mean {scoring.upper()}: {scores.mean():.3f} +/- {scores.std():.3f}")
    print(f"95% Confidence Interval: [{scores.mean() - 1.96*scores.std():.3f}, "
          f"{scores.mean() + 1.96*scores.std():.3f}]")
    return scores