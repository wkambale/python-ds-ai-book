import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

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
    return keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
        layers.RandomContrast(0.1)
    ])

def visualize_augmentations(image: np.ndarray, augmentation_model: keras.Sequential, num_samples: int = 5) -> None:
    """
    Visualize augmented versions of a single image.
    """
    plt.figure(figsize=(12, 3))
    for i in range(num_samples):
        ax = plt.subplot(1, num_samples, i + 1)
        augmented = augmentation_model(tf.expand_dims(image, 0), training=True)
        ax.imshow(augmented[0])
        ax.set_title(f"Augmented {i+1}")
        ax.axis("off")

    plt.tight_layout()
    plt.show()

data_augmentation = create_augmentation_layer()