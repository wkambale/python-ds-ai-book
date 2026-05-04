# Visualize sample digits
def plot_sample_digits(X: np.ndarray,
                       y: np.ndarray,
                       n_samples: int = 10) -> None:
    """Display a row of sample digits with their labels."""
    fig, axes = plt.subplots(1, n_samples, figsize=(12, 2))
    for i, ax in enumerate(axes):
        ax.imshow(X[i], cmap="binary")
        ax.axis('off')
        ax.set_title(f"Label: {y[i]}")
    plt.tight_layout()
    plt.show()

plot_sample_digits(X_train, y_train)