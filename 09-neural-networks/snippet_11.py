def save_model(model: keras.Model,
               filepath: str,
               include_optimizer: bool = True) -> None:
    """
    Save a trained Keras model.

    Args:
        model: Trained Keras model
        filepath: Path to save the model (use .keras extension)
        include_optimizer: Whether to save optimizer state for continued training
    """
    model.save(filepath, include_optimizer=include_optimizer)
    print(f"Model saved to {filepath}")

def load_trained_model(filepath: str) -> keras.Model:
    """Load a previously saved model."""
    model = keras.models.load_model(filepath)
    print(f"Model loaded from {filepath}")
    return model

# Save the model
save_model(model_robust, 'mnist_classifier.keras')

# Later, load it back
# loaded_model = load_trained_model('mnist_classifier.keras')