def predict_and_display(model: keras.Model,
                        X: np.ndarray,
                        y_true: np.ndarray,
                        n_samples: int = 5) -> None:
    """Make predictions and display results with confidence scores."""
    X_sample = X[:n_samples]
    y_proba = model.predict(X_sample, verbose=0)
    y_pred = np.argmax(y_proba, axis=-1)

    fig, axes = plt.subplots(1, n_samples, figsize=(12, 3))
    for i, ax in enumerate(axes):
        ax.imshow(X_sample[i], cmap="binary")
        ax.axis('off')
        confidence = y_proba[i, y_pred[i]] * 100
        color = 'green' if y_pred[i] == y_true[i] else 'red'
        ax.set_title(f"Pred: {y_pred[i]} ({confidence:.1f}%)\nTrue: {y_true[i]}",
                     color=color)
    plt.tight_layout()
    plt.show()

predict_and_display(model, X_test_norm, y_test)