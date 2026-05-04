def encode_categorical_features(
    X: pd.DataFrame,
    categorical_columns: List[str],
    drop_first: bool = True
) -> pd.DataFrame:
    """
    One-hot encodes categorical columns in a DataFrame.

    Args:
        X: Feature DataFrame.
        categorical_columns: List of columns to encode.
        drop_first: Whether to drop the first category to avoid multicollinearity.

    Returns:
        DataFrame with categorical columns one-hot encoded.
    """
    return pd.get_dummies(X, columns=categorical_columns, drop_first=drop_first)

# Identify categorical columns
categorical_columns = X.select_dtypes(include=['object']).columns.tolist()
print(f"Categorical columns to encode: {categorical_columns}")

# Perform one-hot encoding
X_encoded = encode_categorical_features(X, categorical_columns, drop_first=True)

print(f"\nOriginal shape: {X.shape}")
print(f"Encoded shape: {X_encoded.shape}")
print(f"\nNew columns after encoding:")
print([col for col in X_encoded.columns if 'location' in col])