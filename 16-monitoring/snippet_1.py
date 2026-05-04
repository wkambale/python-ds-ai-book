# Check for disparate impact across segments
def check_segment_performance(
    predictions_df: pd.DataFrame,
    segment_column: str,
    metrics: list = ['accuracy', 'false_positive_rate']
) -> pd.DataFrame:
    """
    Calculate metrics per segment to detect fairness issues.
    """
    results = []
    for segment in predictions_df[segment_column].unique():
        segment_data = predictions_df[predictions_df[segment_column] == segment]
        segment_metrics = {
            'segment': segment,
            'n_samples': len(segment_data)
        }

        # Calculate metrics...
        results.append(segment_metrics)

    return pd.DataFrame(results)