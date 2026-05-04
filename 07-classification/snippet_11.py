from imblearn.over_sampling import SMOTE

def apply_smote_and_evaluate(
    X_train: np.ndarray,
    X_test: np.ndarray,
    y_train: pd.Series,
    y_test: pd.Series
) -> Tuple[np.ndarray, pd.Series, pd.DataFrame]:
    """
    Applies SMOTE to training data and compares model performance.

    Args:
        X_train: Training features.
        X_test: Test features.
        y_train: Training labels.
        y_test: Test labels.
    """
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    
    # Train model on resampled data
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_resampled, y_train_resampled)
    y_pred = model.predict(X_test)
    
    results = []
    results.append({
        'Model': 'SMOTE Resampled',
        'Recall (Churn)': recall_score(y_test, y_pred),
        'Precision (Churn)': precision_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred)
    })

    return X_train_resampled, y_train_resampled, pd.DataFrame(results)

# Apply SMOTE
X_train_smote, y_train_smote, smote_comparison = apply_smote_and_evaluate(
    X_train_scaled, X_test_scaled, y_train, y_test
)
print("\nPerformance Comparison:")
print(smote_comparison.to_string(index=False))