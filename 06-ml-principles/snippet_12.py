from sklearn.model_selection import cross_val_score

    model,
    X: np.ndarray,
    y: pd.Series,
    cv: int = 5,
    scoring: str = 'f1'
) -> None:
    """
    Performs k-fold cross-validation and reports results.

    Args:
        model: Scikit-learn model (will be cloned for each fold).
        X: Feature matrix.
        y: Target vector.
        cv: Number of folds.
        scoring: Metric to evaluate.
    """

          f"{scores.mean() + 1.96*scores.std():.3f}]")