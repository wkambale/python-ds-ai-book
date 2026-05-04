from sklearn.model_selection import train_test_split

def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
    stratify: bool = True
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits data into training and testing sets.

    Args:
        X: Feature matrix.
        y: Target vector.
        test_size: Proportion of the dataset to include in the test split.
        random_state: Seed used by the random number generator.

    Returns:
        Tuple containing X_train, X_test, y_train, y_test.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=test_size, 
        random_state=random_state, 
        stratify=y
    )
    return X_train, X_test, y_train, y_test

# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = split_data(X, y)

print("Data shapes after splitting:")
print(f"  X_train: {X_train.shape}")
print(f"  X_test:  {X_test.shape}")
print(f"  y_train: {y_train.shape}")
print(f"  y_test:  {y_test.shape}")

print(f"\nClass distribution in training set:")
print(y_train.value_counts(normalize=True))
print(f"\nClass distribution in test set:")
print(y_test.value_counts(normalize=True))