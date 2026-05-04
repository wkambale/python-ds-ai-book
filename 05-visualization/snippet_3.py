import pandas as pd
import numpy as np

def load_and_prepare_mobicash_data(filepath: str) -> pd.DataFrame:
    """
    Loads and prepares MobiCash data for visualization.

    Args:
        filepath: Path to the CSV file.

    Returns:
        Cleaned DataFrame with additional features for visualization.
    """
    df = pd.read_csv(filepath, parse_dates=['timestamp'])

    # Engineer time-based features
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    
    # Calculate transaction fees (1.5% of amount)
    df['transaction_fee'] = df['amount_ugx'] * 0.015
    
    # Categorize transaction size
    df['size_category'] = pd.cut(
        df['amount_ugx'], 
        bins=[0, 10000, 50000, 100000, float('inf')],
        labels=['Micro', 'Small', 'Medium', 'Large']
    )

    # Rename amount column for clarity
    df = df.rename(columns={'amount_ugx': 'amount'})

    return df

# Load the data
df_clean = load_and_prepare_mobicash_data('mobicash_transactions.csv')
print(f"Loaded {len(df_clean)} transactions")
print(f"Date range: {df_clean.index.min()} to {df_clean.index.max()}")