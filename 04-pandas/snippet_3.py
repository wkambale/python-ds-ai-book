import pandas as pd
import numpy as np

# Load the dataset with explicit configuration
df = pd.read_csv(
    'mobicash_transactions.csv',
    parse_dates=['timestamp'],      # Parse timestamp as datetime
    na_values=['NULL', '', 'N/A'],  # Treat these as missing values
    dtype={'transaction_id': str, 'customer_id': str}  # Ensure IDs stay as strings
)