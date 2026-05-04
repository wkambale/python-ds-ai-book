from sklearn.preprocessing import StandardScaler

def scale_features(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray, StandardScaler]:
    """
    Scales features using standardization.
    Fits the scaler on training data only, then transforms both sets.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)