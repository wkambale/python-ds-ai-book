def build_mlp_classifier(input_shape: Tuple[int, int] = (28, 28),
                         hidden_units: list[int] = [300, 100],
                         num_classes: int = 10) -> keras.Model:
    """
    Build a Multi-Layer Perceptron for image classification.

    Args:
        input_shape: Shape of input images (height, width)
        hidden_units: List of neurons in each hidden layer
        num_classes: Number of output classes

    Returns:
        Compiled Keras model
    """
    layers = [
        # Flatten: Converts 2D image into 1D array
        keras.layers.Flatten(input_shape=input_shape)
    ]

    # Add hidden layers with ReLU activation
    for units in hidden_units:
        layers.append(keras.layers.Dense(units, activation="relu"))

    # Output layer with softmax for multi-class classification
    layers.append(keras.layers.Dense(num_classes, activation="softmax"))

    return keras.models.Sequential(layers)

model = build_mlp_classifier()
model.summary()