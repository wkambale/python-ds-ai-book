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

    if train_score < 0.6:  # Arbitrary threshold for "good"
    elif gap > threshold:
    else: