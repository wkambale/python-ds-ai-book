def train_cnn(model: keras.Model,
              X_train: np.ndarray,
              y_train: np.ndarray,
              X_val: np.ndarray,
              y_val: np.ndarray,
              epochs: int = 20,
              batch_size: int = 64) -> keras.callbacks.History:
    """
    Train a CNN with early stopping.

    Args:
        model: Compiled Keras model
        X_train, y_train: Training data
        X_val, y_val: Validation data
        epochs: Maximum training epochs
    """
    early_stopping = EarlyStopping(
        monitor='val_accuracy',
        patience=10,
        restore_best_weights=True
    )
    
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        validation_data=(X_val, y_val),
        callbacks=[early_stopping],
        batch_size=64,
        verbose=1
    )
    return history

# Split training data to create validation set
X_train_split, X_val = X_train[:45000], X_train[45000:]
y_train_split, y_val = y_train[:45000], y_train[45000:]

# Train the model
history = train_cnn(model, X_train_split, y_train_split, X_val, y_val)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.4f}")