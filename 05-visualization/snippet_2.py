def plot_anscombes_quartet(data: pd.DataFrame) -> None:
    """
    Creates a 2x2 grid of scatter plots for Anscombe's Quartet.

    Args:
        data: DataFrame containing Anscombe's Quartet with columns
              'dataset', 'x', and 'y'.
    """
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Anscombe's Quartet: Why We Visualize", fontsize=14, fontweight='bold')

    datasets = ['I', 'II', 'III', 'IV']
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for dataset_name, (row, col) in zip(datasets, positions):
        subset = data[data['dataset'] == dataset_name]
        ax = axes[row, col]
        ax.scatter(subset['x'], subset['y'], s=50, alpha=0.7)
        ax.set_title(f"Dataset {dataset_name}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_xlim(2, 20)
        ax.set_ylim(2, 14)

    plt.tight_layout()
    plt.show()

plot_anscombes_quartet(anscombe)