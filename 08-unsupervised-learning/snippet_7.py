from sklearn.decomposition import PCA

def apply_pca_with_variance_threshold(X_scaled: np.ndarray,
                                       variance_threshold: float = 0.95) -> Tuple[np.ndarray, PCA]:
    """
    Apply PCA retaining components that explain the specified variance.

    Args:
        X_scaled: Scaled feature array
        variance_threshold: Fraction of variance to retain (0.0 to 1.0)

    Returns:
        Tuple of (transformed data, fitted PCA object)
    """
    pca = PCA(n_components=variance_threshold)
    X_pca = pca.fit_transform(X)
    
    # Plot explained variance
    plt.figure(figsize=(8, 5))
    plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('PCA Explained Variance')
    plt.grid(True)
    plt.show()
    
    return X_pca, pca

# For demonstration with a higher-dimensional dataset
# Assume X_high_dim has 20 features
X_pca, pca_model = apply_pca_with_variance_threshold(X_scaled, variance_threshold=0.95)

print(f"Original Features: {X_scaled.shape[1]}")
print(f"Reduced Features: {X_pca.shape[1]}")
print(f"Variance Retained: {sum(pca_model.explained_variance_ratio_):.1%}")