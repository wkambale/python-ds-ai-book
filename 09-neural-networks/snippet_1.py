import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

print(f"TensorFlow Version: {tf.__version__}")

def load_mnist() -> Tuple[Tuple[np.ndarray, np.ndarray],
                          Tuple[np.ndarray, np.ndarray]]:
    """
    Load and return the MNIST dataset.

    Returns:
        Tuple of (train_data, test_data), where each is (images, labels)
    """
    return keras.datasets.mnist.load_data()

(X_train_full, y_train_full), (X_test, y_test) = load_mnist()

print(f"Training Data Shape: {X_train_full.shape}")
print(f"Test Data Shape: {X_test.shape}")
print(f"Pixel value range: [{X_train_full.min()}, {X_train_full.max()}]")