from sklearn.metrics import classification_report, precision_score, recall_score, f1_score

def evaluate_model(
    y_true: pd.Series,
    y_pred: np.ndarray,
    target_names: list = None
) -> dict:
    """
    Evaluates a classification model and prints a detailed report.

    Args:
        y_true: Actual labels.
        y_pred: Predicted labels.
        target_names: Names for each class.
        
    Returns:
        Dictionary of key metrics.
    """
    print("CLASSIFICATION REPORT")
    print(classification_report(y_true, y_pred, target_names=target_names))
    
    metrics = {
        'precision': precision_score(y_true, y_pred),
        'recall': recall_score(y_true, y_pred),
        'f1': f1_score(y_true, y_pred)
    }
    
    print("Key metrics for the CHURN class:")
    print(f"  Precision: {metrics['precision']*100:.2f}%")
    print(f"  Recall:    {metrics['recall']*100:.2f}%")
    print(f"  F1-Score:  {metrics['f1']*100:.2f}%")
    
    return metrics

metrics = evaluate_model(y_test, y_pred, target_names=['No Churn', 'Churn'])