from sklearn.neighbors import KNeighborsClassifier

def train_and_evaluate_knn(
    X_train: np.ndarray,
    X_test: np.ndarray,
    y_train: pd.Series,
    y_test: pd.Series,
    k_values: List[int]
) -> pd.DataFrame:
    """
    Trains KNN models with different k values and compares performance.

    Args:
        X_train: Scaled training features.
        X_test: Scaled test features.
        y_train: Training labels.
        y_test: Test labels.
        k_values: List of k values to test.
    """
    results = []
    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        
        results.append({
            'k': k,
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred, zero_division=0),
            'Recall': recall_score(y_test, y_pred),
            'F1-Score': f1_score(y_test, y_pred)
        })
        
    return pd.DataFrame(results)

# Evaluate different k values
k_values = [3, 5, 7, 9, 11, 15, 21]
knn_results = train_and_evaluate_knn(
    X_train_scaled, X_test_scaled, y_train, y_test, k_values
)

print("KNN Performance by k Value:")
print(knn_results.round(3).to_string(index=False))