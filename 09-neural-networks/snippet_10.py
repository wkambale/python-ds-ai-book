def train_with_early_stopping(model: keras.Model,
                               X_train: np.ndarray,
                               y_train: np.ndarray,
                               X_valid: np.ndarray,
                               y_valid: np.ndarray,
                               patience: int = 5,
                               max_epochs: int = 50) -> keras.callbacks.History:
    """
    Train model with early stopping to prevent overfitting.

    Args:
        model: Compiled Keras model
        X_train, y_train: Training data
        X_val, y_val: Validation data
        epochs: Maximum training epochs
    """
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    )
    
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        validation_data=(X_val, y_val),
        callbacks=[early_stopping],
        verbose=1
    )

    return history

history_robust = train_with_early_stopping(
    model_robust, X_train, y_train, X_valid, y_valid
)