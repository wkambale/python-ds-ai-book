import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def load_and_preprocess_cifar10() -> Tuple[Tuple[np.ndarray, np.ndarray],
                                            Tuple[np.ndarray, np.ndarray]]:
    """
    Load CIFAR-10 dataset and normalize pixel values.

    Returns:
        Tuple of ((X_train, y_train), (X_test, y_test)) with normalized values
    """
    (X_train_full, y_train_full), (X_test, y_test) = cifar10.load_data()
    
    X_train_full = X_train_full.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0
    
    # Convert class vectors to binary class matrices
    y_train_full = to_categorical(y_train_full, 10)
    y_test = to_categorical(y_test, 10)
    
    return (X_train_full, y_train_full), (X_test, y_test)

(X_train, y_train), (X_test, y_test) = load_and_preprocess_cifar10()

# Build and compile model
model = build_basic_cnn()
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()