from sklearn.svm import SVC

def train_svm_models(
    X_train: np.ndarray,
    X_test: np.ndarray,
    y_train: pd.Series,
    y_test: pd.Series
) -> Dict[str, Dict[str, float]]:
    """
    Trains SVM models with different kernels and compares performance.

    Args:
        X_train: Scaled training features.
        X_test: Scaled test features.
        y_train: Training labels.
        y_test: Test labels.
    """
    results = {}
    kernels = ['linear', 'rbf']
    
    for kernel in kernels:
        svm = SVC(kernel=kernel, probability=True, random_state=42)
        svm.fit(X_train, y_train)
        y_pred = svm.predict(X_test)
        
        results[kernel] = {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred, zero_division=0),
            'Recall': recall_score(y_test, y_pred),
            'F1-Score': f1_score(y_test, y_pred)
        }
        
    return results

# Train and evaluate SVMs
svm_results = train_svm_models(X_train_scaled, X_test_scaled, y_train, y_test)

print("SVM Performance by Kernel:")
for kernel, metrics in svm_results.items():
    print(f"\n{kernel.upper()} Kernel:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.3f}")