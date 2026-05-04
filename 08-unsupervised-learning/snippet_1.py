import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from typing import Tuple

def load_and_scale_data(filepath: str,
                        feature_cols: list[str]) -> Tuple[pd.DataFrame, np.ndarray, StandardScaler]:
    """
    Load data and apply standard scaling for clustering.

    Args:
        filepath: Path to CSV file
        feature_cols: List of column names to use as features
    """
    df = pd.read_csv(filepath)
    X = df[feature_cols].copy()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return df, X_scaled, scaler

# Fit K-Means with 3 clusters (initial guess)
kmeans_model, clusters = fit_kmeans(X_scaled, n_clusters=3)

# Add labels back to original data for interpretation
data['Cluster'] = clusters

print("Cluster Centers (Averages)")
print(data.groupby('Cluster')[feature_columns].mean())