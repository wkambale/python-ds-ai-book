from sklearn.manifold import TSNE

def apply_tsne(X_scaled: np.ndarray,
               perplexity: int = 30,
               random_state: int = 42) -> np.ndarray:
    """
    Apply t-SNE for 2D visualization.

    Args:
        X_scaled: Scaled feature array
        perplexity: Balance between local and global structure (5-50 typical)
        random_state: Random seed for reproducibility

    Returns:
        2D transformed coordinates
    """
    tsne = TSNE(n_components=2, random_state=random_state, perplexity=perplexity)
    return tsne.fit_transform(X_scaled)

# t-SNE is computationally expensive, so we typically use it on smaller samples
X_tsne = apply_tsne(X_scaled, perplexity=30)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
                      c=data['Cluster'], cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.title('t-SNE Visualization of Customer Clusters')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()