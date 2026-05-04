import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mobicash_data(n_transactions: int = 50, seed: int = 42) -> pd.DataFrame:
    """
    Generates a synthetic MobiCash transaction dataset.

    Args:
        n_transactions: Number of transactions to generate.
        seed: Random seed for reproducibility.

    Returns:
        DataFrame containing synthetic transaction data.
    """
    np.random.seed(seed)
    
    # Generate basic fields
    transaction_ids = [f"TXN{i:05d}" for i in range(n_transactions)]
    timestamps = pd.date_range(start='2023-01-01', periods=n_transactions, freq='H')
    amounts = np.random.lognormal(mean=9, sigma=1.5, size=n_transactions).round(-2)
    types = np.random.choice(['Transfer', 'Payment', 'Withdrawal', 'Deposit'], size=n_transactions)
    sender_ids = [f"USR{np.random.randint(1000, 9999)}" for _ in range(n_transactions)]
    receiver_ids = [f"USR{np.random.randint(1000, 9999)}" for _ in range(n_transactions)]
    agent_ids = [f"AGT{np.random.randint(100, 999)}" if t in ['Withdrawal', 'Deposit'] else None for t in types]
    agent_locations = [np.random.choice(['Kampala', 'Entebbe', 'Gulu', 'Mbarara']) if a else None for a in agent_ids]
    
    data = {
        'transaction_id': transaction_ids,
        'timestamp': timestamps,
        'amount_ugx': amounts,
        'transaction_type': types,
        'sender_id': sender_ids,
        'receiver_id': receiver_ids,
    }
    data['agent_id'] = agent_ids
    data['agent_location'] = agent_locations

    return pd.DataFrame(data)

# Generate and save the dataset
df_raw = generate_mobicash_data(50)
df_raw.to_csv('mobicash_transactions.csv', index=False)
print(f"Generated {len(df_raw)} transactions")
print(df_raw.head())