def diagnose_fit(train_score: float, test_score: float, threshold: float = 0.1) -> str:
    """
    Diagnoses whether a model is underfitting, overfitting, or well-fit.

    Args:
        train_score: Model performance on training data (e.g., accuracy).
        test_score: Model performance on test data.
        threshold: Maximum acceptable gap between train and test scores.

    Returns:
        Diagnosis string.
    """
    gap = train_score - test_score
    if train_score < 0.6:
        return "Underfitting: The model is not learning the training data well."
    elif gap > threshold:
        return "Overfitting: High training performance but significantly worse on test."
    else:
        return "Well-fit: Training and test performance are balanced."