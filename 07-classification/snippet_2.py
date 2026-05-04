def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Computes the sigmoid function.

    Args:
        z: Input values (can be scalar or array).

    Returns:
        Sigmoid of input, values between 0 and 1.
    """
    return 1 / (1 + np.exp(-z))

# Visualize the sigmoid function
z_values = np.linspace(-10, 10, 100)
sigmoid_values = sigmoid(z_values)

plt.figure(figsize=(10, 5))
plt.plot(z_values, sigmoid_values, 'b-', linewidth=2)
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
plt.xlabel('z (linear combination of features)', fontsize=11)
plt.ylabel('σ(z) (probability)', fontsize=11)
plt.title('The Sigmoid Function: Mapping Any Value to [0, 1]', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim(-0.1, 1.1)

# Annotate key points
plt.annotate('P = 0.5 when z = 0', xy=(0, 0.5), xytext=(2, 0.6),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=10)
plt.tight_layout()
plt.show()