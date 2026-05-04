def compare_class_weights(
    X_train: np.ndarray,
    X_test: np.ndarray,
    y_train: pd.Series,
    y_test: pd.Series
) -> pd.DataFrame:
    """
    Compares model performance with and without class weighting.

    Args:
        X_train: Training features.
        X_test: Test features.
        y_train: Training labels.
        y_test: Test labels.
    """
    results = []
    
    # Unweighted model
    model_unweighted = RandomForestClassifier(random_state=42)
    model_unweighted.fit(X_train, y_train)
    y_pred_un = model_unweighted.predict(X_test)
    
    # Weighted model
    model_weighted = RandomForestClassifier(class_weight='balanced', random_state=42)
    model_weighted.fit(X_train, y_train)
    y_pred_w = model_weighted.predict(X_test)
    
    for name, y_pred in [('Unweighted', y_pred_un), ('Class_Weight="balanced"', y_pred_w)]:
        results.append({
            'Model': name,
            'Recall (Churn)': recall_score(y_test, y_pred),
            'Precision (Churn)': precision_score(y_test, y_pred),
            'F1-Score': f1_score(y_test, y_pred)
        })

    return pd.DataFrame(results)

# Compare weighted vs unweighted
weight_comparison = compare_class_weights(
    X_train_scaled, X_test_scaled, y_train, y_test
)
print("Effect of Class Weights:")
print(weight_comparison.to_string(index=False))