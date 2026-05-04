def preprocess_mnist(X_train_full: np.ndarray,
                     X_test: np.ndarray,
                     y_train_full: np.ndarray,
                     validation_size: int = 5000) -> dict:
    """
    Preprocess MNIST data: normalize and split into train/validation/test.

    Args:
        X_train_full: Full training images
        X_test: Test images
        y_train_full: Full training labels
        validation_size: Number of samples for validation set

    Returns:
        Dictionary containing all processed datasets
    """
    # Normalize pixel values
    X_train_full = X_train_full.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    
    # Validation split
    X_train, X_valid = X_train_full[validation_size:], X_train_full[:validation_size]
    y_train, y_valid = y_train_full[validation_size:], y_train_full[:validation_size]
    
    return {
        'X_train': X_train,
        'y_train': y_train,
        'X_valid': X_valid,
        'y_valid': y_valid,
        'X_test': X_test,
        'y_test': y_test
    }

data = preprocess_mnist(X_train_full, X_test, y_train_full)
X_train, X_valid = data['X_train'], data['X_valid']
y_train, y_valid = data['y_train'], data['y_valid']
X_test_norm = data['X_test']

print(f"Training set: {X_train.shape[0]} samples")
print(f"Validation set: {X_valid.shape[0]} samples")
print(f"Test set: {X_test_norm.shape[0]} samples")