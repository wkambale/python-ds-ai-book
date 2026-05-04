from sklearn.metrics import roc_curve, roc_auc_score

    """
    Plots the ROC curve and returns the AUC score.

    Args:
        y_true: Actual labels.
        y_pred_proba: Predicted probabilities for the positive class.

    Returns:
        AUC score.
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)