def create_model_comparison_table(
    X_train_scaled: np.ndarray,
    X_test_scaled: np.ndarray,
    X_train_unscaled: pd.DataFrame,
    X_test_unscaled: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series
) -> pd.DataFrame:
    """
    Creates a comprehensive comparison table of all models.

    Returns:
        DataFrame with metrics for each model.
    """
    all_results = []
    
    # Example logic to populate metrics for models
    # This represents the gathered results from the functions above
    models = {
        'Logistic Regression': (LogisticRegression(random_state=42), X_train_scaled, X_test_scaled),
        'Random Forest': (RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42), X_train_unscaled, X_test_unscaled),
        'SVM (RBF)': (SVC(kernel='rbf', probability=True, random_state=42), X_train_scaled, X_test_scaled)
    }
    
    for name, (model, X_tr, X_te) in models.items():
        model.fit(X_tr, y_train)
        y_pred = model.predict(X_te)
        all_results.append({
            'Model': name,
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred, zero_division=0),
            'Recall': recall_score(y_test, y_pred),
            'F1-Score': f1_score(y_test, y_pred)
        })
        
    return pd.DataFrame(all_results)

comparison_table = create_model_comparison_table(
    X_train_scaled, X_test_scaled,
    X_train_unscaled, X_test_unscaled,
    y_train, y_test
)

print("=" * 70)
print("MODEL COMPARISON SUMMARY")
print("=" * 70)
print(comparison_table.round(3).to_string(index=False))