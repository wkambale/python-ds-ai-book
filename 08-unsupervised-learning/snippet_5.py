from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

def find_optimal_eps(X_scaled: np.ndarray, min_samples: int = 5) -> None:
    """
    Plot k-distance graph to help choose eps parameter.
    The 'elbow' in this plot suggests a good eps value.
    """
    neighbors = NearestNeighbors(n_neighbors=min_samples)
    neighbors.fit(X_scaled)
    distances, _ = neighbors.kneighbors(X_scaled)

    k_distances = np.sort(distances[:, min_samples - 1])

    plt.figure(figsize=(8, 5))
    plt.plot(k_distances)
    plt.xlabel('Points (sorted by distance)')
    plt.ylabel(f'Distance to {min_samples}th nearest neighbor')
    plt.title('K-Distance Graph for eps Selection')
    plt.grid(True)
    plt.show()

find_optimal_eps(X_scaled, min_samples=5)

dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters_db = dbscan.fit_predict(X_scaled)

print(pd.Series(clusters_db).value_counts().sort_index())