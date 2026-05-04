def build_augmented_cnn(input_shape: Tuple[int, int, int] = (32, 32, 3),
                        num_classes: int = 10) -> keras.Model:
    """
    Build a CNN with integrated data augmentation.
    Data augmentation is applied only during training.
    """
    model = models.Sequential([
        create_augmentation_layer(),

        layers.Conv2D(32, (3, 3), activation='relu',
                      padding='same', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])

    return model