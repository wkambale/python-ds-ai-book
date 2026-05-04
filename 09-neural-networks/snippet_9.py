def build_robust_mlp(input_shape: Tuple[int, int] = (28, 28),
                     hidden_units: list[int] = [300, 100],
                     dropout_rate: float = 0.2,
                     num_classes: int = 10) -> keras.Model:
    """
    Build an MLP with dropout regularization.

    Args:
        input_shape: Shape of input images
        hidden_units: Neurons per hidden layer
        dropout_rate: Fraction of neurons to drop (0.0 to 1.0)
        num_classes: Number of output classes

    Returns:
        Keras model with dropout layers
    """
    layers = [keras.layers.Flatten(input_shape=input_shape)]

    for units in hidden_units:
        layers.append(keras.layers.Dense(units, activation="relu"))
        layers.append(keras.layers.Dropout(rate=dropout_rate))

    layers.append(keras.layers.Dense(num_classes, activation="softmax"))

    return keras.models.Sequential(layers)

model_robust = build_robust_mlp(dropout_rate=0.2)
model_robust.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)