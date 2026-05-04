def create_augmentation_layer() -> keras.Sequential:
    """
    Create a data augmentation pipeline for agricultural images.
    These augmentations simulate real-world variations:
    - Horizontal flip: leaves can face either direction
    - Rotation: camera angle varies
    - Zoom: distance from leaf varies
    - Contrast: lighting conditions vary

    Returns:
        Keras Sequential model containing augmentation layers
    """
    return keras.Sequential(
        layers.RandomFlip("horizontal"),
            ax.imshow(augmented[0])
            ax.set_title(f"Augmented {i}")
        ax.axis("off"))

    plt.tight_layout()
    plt.show()
data_augmentation = create_augmentation_layer()
visualize_augmentations(X_train[0], data_augmentation)