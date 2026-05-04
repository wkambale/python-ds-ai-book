from sklearn.ensemble import RandomForestClassifier

def train_random_forest(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    n_estimators: int = 100,
    max_depth: int = 10
) -> Tuple[RandomForestClassifier, Dict[str, float]]:
    """
    Trains a Random Forest classifier.

    Args:
        X_train: Training features (scaling not required).
        X_test: Test features.
        y_train: Training labels.
        y_test: Test labels.
        n_estimators: Number of trees.
        max_depth: Maximum depth of trees.
    """
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, zero_division=0),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred)
    }
    return model, metrics

# Train Random Forest
model_rf, rf_metrics = train_random_forest(
    X_train_unscaled, X_test_unscaled, y_train, y_test,
    n_estimators=100, max_depth=10
)

print("Random Forest Performance:")
for metric, value in rf_metrics.items():
    print(f"  {metric}: {value:.3f}")