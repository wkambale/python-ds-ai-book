def fine_tune_model(model: keras.Model,
                    base_model: keras.Model,
                    num_layers_to_unfreeze: int = 30,
                    fine_tune_lr: float = 1e-5) -> None:
    """
    Prepare model for fine-tuning by unfreezing top layers.

    Args:
        model: The complete model
        base_model: The pre-trained base model within it
        num_layers_to_unfreeze: Number of top layers to unfreeze
        fine_tune_lr: Learning rate for fine-tuning (should be very small)
    """
    # Unfreeze the base model
    base_model.trainable = True

    # Freeze all layers except the top N
    for layer in base_model.layers[:-num_layers_to_unfreeze]:
        layer.trainable = False

    # Recompile with lower learning rate
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=fine_tune_lr),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    print(f"Fine-tuning: {num_layers_to_unfreeze} layers unfrozen")
    print(f"Learning rate: {fine_tune_lr}")