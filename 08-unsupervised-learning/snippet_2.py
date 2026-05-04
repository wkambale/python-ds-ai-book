def compute_inertia_curve(X_scaled: np.ndarray,
                          k_range: range,
                          random_state: int = 42) -> list[float]:
    """
    Compute inertia values for a range of cluster counts.

    Args:
        X_scaled: Scaled feature array
        k_range: Range of K values to try
        random_state: Random seed for reproducibility

    Returns:
        List of inertia values corresponding to each K
    """
    inertia = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        km.fit(X_scaled)
        inertia.append(km.inertia_)
    return inertia

k_range = range(1, 11)
inertia_values = compute_inertia_curve(X_scaled, k_range)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia_values, marker='o')
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.grid(True)
plt.show()