from sklearn.metrics import silhouette_score

def evaluate_cluster_counts(X_scaled: np.ndarray,
                            k_values: list[int],
                            random_state: int = 42) -> dict[int, float]:
    """
    Evaluate silhouette scores for different cluster counts.

    Args:
        X_scaled: Scaled feature array
        k_values: List of K values to evaluate
        random_state: Random seed for reproducibility

    Returns:
        Dictionary mapping K to silhouette score
    """
    scores = {}
    for k in k_values:
        km = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        labels = km.fit_predict(X_scaled)
        scores[k] = silhouette_score(X_scaled, labels)
    return scores

silhouette_scores = evaluate_cluster_counts(X_scaled, [2, 3, 4, 5])

for k, score in silhouette_scores.items():
    print(f"For n_clusters = {k}, the Silhouette Score is: {score:.3f}")