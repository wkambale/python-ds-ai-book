from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def plot_confusion_matrix(
    y_true: pd.Series,
    y_pred: np.ndarray,
    labels: list = None
) -> None:
    """
    Plots a confusion matrix with annotations.

    Args:
        y_true: Actual labels.
        y_pred: Predicted labels.
        labels: Class names.
    """
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues', values_format='d')
    plt.title('Confusion Matrix')
    plt.show()

y_pred = model_logreg.predict(X_test)
plot_confusion_matrix(y_test, y_pred, labels=['No Churn', 'Churn'])