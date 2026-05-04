from sklearn.metrics import roc_curve, roc_auc_score

def plot_roc_comparison(
    models: Dict[str, Any],
    X_test: np.ndarray,
    y_test: pd.Series
) -> None:
    """
    Plots ROC curves for multiple models on the same graph.

    Args:
        models: Dictionary of {model_name: trained_model}.
        X_test: Test features.
        y_test: Test labels.
    """
    plt.figure(figsize=(10, 8))
    
    for name, model in models.items():
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        auc = roc_auc_score(y_test, y_pred_proba)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})')
        
    plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Comparison')
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3)
    plt.show()

# Create a dictionary to hold models to compare
models_to_compare = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNN (k=11)': KNeighborsClassifier(n_neighbors=11),
    'SVM (RBF)': SVC(kernel='rbf', probability=True, random_state=42)
}

# Train them
for name, model in models_to_compare.items():
    model.fit(X_train_scaled, y_train)

# Plot ROC curves (using scaled data for non-tree models)
# Note: For fair comparison, we'd need to handle this more carefully
plot_roc_comparison(
    {'Logistic Regression': models_to_compare['Logistic Regression'],
     'KNN (k=11)': models_to_compare['KNN (k=11)'],
     'SVM (RBF)': models_to_compare['SVM (RBF)']},
    X_test_scaled, y_test
)