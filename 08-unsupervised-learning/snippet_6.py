def flag_anomalies_for_review(data: pd.DataFrame,
                               cluster_labels: np.ndarray,
                               id_column: str = 'user_id') -> pd.DataFrame:
    """
    Extract anomalous records for manual review.

    Args:
        data: Original dataframe with user information
        cluster_labels: DBSCAN cluster assignments (-1 indicates anomaly)
        id_column: Column name containing user identifiers

    Returns:
        DataFrame of flagged records requiring investigation
    """
    data_with_clusters = data.copy()
    data_with_clusters['cluster'] = cluster_labels
    data_with_clusters['is_anomaly'] = cluster_labels == -1

    anomalies = data_with_clusters[data_with_clusters['is_anomaly']]

    return anomalies[[id_column, 'avg_transaction_amount',
                      'frequency_score', 'cluster']]

# Flag suspicious accounts
flagged_accounts = flag_anomalies_for_review(data, clusters_db)
print(f"Accounts flagged for review: {len(flagged_accounts)}")