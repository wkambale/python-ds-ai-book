def interpret_logistic_coefficients(
    model: LogisticRegression,
    feature_names: List[str]
) -> pd.DataFrame:
    """
    Extracts and interprets logistic regression coefficients.

    Args:
        model: Trained logistic regression model.
        feature_names: Names of features in order.

    Returns:
        DataFrame with coefficients sorted by importance.
    """
    coef_df = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_[0],
        'Odds_Ratio': np.exp(model.coef_[0])
    })

    coef_df['Abs_Coefficient'] = coef_df['Coefficient'].abs()
    coef_df = coef_df.sort_values('Abs_Coefficient', ascending=False)

    return coef_df.drop('Abs_Coefficient', axis=1)

# Get coefficient interpretation
coef_interpretation = interpret_logistic_coefficients(
    model_logreg, X_encoded.columns.tolist()
)

print("Logistic Regression Coefficients:")
print(coef_interpretation.to_string(index=False))