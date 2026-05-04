def plot_learning_curves(history: keras.callbacks.History) -> None:
    """Plot training and validation metrics over epochs."""
    metrics_df = pd.DataFrame(history.history)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Loss curves
    axes[0].plot(metrics_df['loss'], label='Training')
    axes[0].plot(metrics_df['val_loss'], label='Validation')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Loss Curves')
    axes[0].legend()
    axes[0].grid(True)

    # Accuracy curves
    axes[1].plot(metrics_df['accuracy'], label='Training')
    axes[1].plot(metrics_df['val_accuracy'], label='Validation')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Accuracy')
    axes[1].set_title('Accuracy Curves')
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

import pandas as pd
plot_learning_curves(history)

# Evaluate on the unseen Test Set
test_loss, test_accuracy = model.evaluate(X_test_norm, y_test)
print(f"Test Accuracy: {test_accuracy:.4f}")