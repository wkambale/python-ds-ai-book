from sklearn.model_selection import train_test_split

def train_sentiment_model(model: keras.Model,
                          X: np.ndarray,
                          y: np.ndarray,
                          epochs: int = 30,
                          validation_split: float = 0.2,
                          patience: int = 5) -> keras.callbacks.History:
    """
    Train the sentiment model with early stopping.

    Args:
        model: Compiled Keras model
        X: Padded input sequences
        y: Binary labels
        epochs: Training epochs
        validation_split: Validation proportion
    """
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    history = model.fit(
        X, y,
        epochs=epochs,
        validation_split=validation_split,
        callbacks=[early_stopping],
        verbose=1
    )

    return history

# Note: With only 8 examples, this is for demonstration only
# A real model needs thousands of examples
history = train_sentiment_model(model, padded_sequences, labels, epochs=20)