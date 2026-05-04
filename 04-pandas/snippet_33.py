def clean_and_transform(filepath: str) -> pd.DataFrame:

    """
    Load, clean, and transform MobiCash transaction data.

    Args:
        filepath: Path to the CSV file.

    Returns:
        Cleaned and transformed DataFrame.
    """
    return (
        pd.read_csv(filepath)
        .dropna(subset=['amount_ugx'])
        .assign(
            timestamp=lambda x: pd.to_datetime(x['timestamp']),
            amount_ugx=lambda x: x['amount_ugx'].astype(float)
        )
        .sort_values('timestamp')
        .reset_index(drop=True)
    )