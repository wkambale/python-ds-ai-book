def create_sequences_for_forecasting(data: np.ndarray,
                                      lookback: int,
                                      forecast_horizon: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create input-output pairs for time series forecasting.

    Args:
        data: 1D array of time series values
        lookback: Number of past time steps to use as input
        forecast_horizon: Number of steps ahead to predict

    Returns:
        Tuple of (X, y) arrays for training
    """
    X, y = [], []
    for i in range(len(data) - lookback):
        X.append(data[i:(i + lookback)])
        y.append(data[i + lookback])
        
    return np.array(X), np.array(y)

lookback = 30  # Use 30 days to predict next day
X, y = create_sequences_for_forecasting(transaction_volume, lookback)
X = X.reshape((X.shape[0], X.shape[1], 1))  # Add feature dimension

# Split (maintaining temporal order - never shuffle time series!)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")