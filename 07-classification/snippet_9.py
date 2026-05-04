def plot_feature_importance(
    model: RandomForestClassifier,
    feature_names: List[str],
    top_n: int = 10
) -> pd.DataFrame:
    """
    Plots and returns feature importances from a Random Forest.

    Args:
        model: Trained Random Forest model.
        feature_names: Names of features.
        top_n: Number of top features to display.
    """
    importances = model.feature_importances_
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Importance', y='Feature', palette='viridis')
    plt.title(f'Top {top_n} Feature Importances')
    plt.tight_layout()
    plt.show()
    
    return importance_df

# Get feature importances
importance_df = plot_feature_importance(
    model_rf, X_encoded.columns.tolist(), top_n=10
)
print("\nFeature Importances:")
print(importance_df.head(10).to_string(index=False))