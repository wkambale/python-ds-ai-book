from sklearn.linear_model import LogisticRegression

def demonstrate_threshold_impact(
    model: LogisticRegression,
    X_test: np.ndarray,
    y_test: pd.Series,
    thresholds: List[float]
) -> pd.DataFrame:
    """
    Shows how different decision thresholds affect precision and recall.

    Args:
        model: Trained logistic regression model.
        X_test: Test features.
        y_test: Test labels.
    """
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    results = []
    
    for threshold in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        y_pred = (y_pred_proba >= threshold).astype(int)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        results.append({
            'Threshold': threshold,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        })
        
    return pd.DataFrame(results)

model_logreg = LogisticRegression(random_state=42, max_iter=1000)
model_logreg.fit(X_train_scaled, y_train)

# Evaluate at different thresholds
thresholds = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
threshold_results = demonstrate_threshold_impact(
    model_logreg, X_test_scaled, y_test, thresholds
)
print("Impact of Decision Threshold on Model Performance:")
print(threshold_results.to_string(index=False))