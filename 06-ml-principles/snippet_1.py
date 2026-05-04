import pandas as pd
import numpy as np
from typing import Tuple

def generate_churn_dataset(
    n_customers: int = 1500,
    churn_rate: float = 0.25,
    seed: int = 42
) -> pd.DataFrame:
    """
    Generates a synthetic customer churn dataset for a mobile money service.

    Args:
        n_customers: Number of customers to generate.
        churn_rate: Proportion of customers who churned (0.0 to 1.0).
    """
    np.random.seed(42)
    n_churned = int(n_customers * churn_rate)
    n_retained = n_customers - n_churned
    
    # Generate retained customers (lower fee, more transactions)
    retained = pd.DataFrame({
        'customer_id': range(1, n_retained + 1),
        'transaction_count': np.random.poisson(25, n_retained),
        'avg_transaction_fee': np.random.normal(500, 100, n_retained),
        'account_age_days': np.random.uniform(100, 1000, n_retained),
        'support_tickets': np.random.poisson(0.5, n_retained),
        'churned': 0
    })
    
    # Generate churned customers (higher fee, fewer transactions)
    churned = pd.DataFrame({
        'customer_id': range(n_retained + 1, n_customers + 1),
        'transaction_count': np.random.poisson(10, n_churned),
        'avg_transaction_fee': np.random.normal(800, 200, n_churned),
        'account_age_days': np.random.uniform(10, 500, n_churned),
        'support_tickets': np.random.poisson(2.5, n_churned),
        'churned': 1
    })
    
    df = pd.concat([retained, churned]).sample(frac=1).reset_index(drop=True)
    return df

# Generate and save the dataset
df_churn = generate_churn_dataset(n_customers=1500, churn_rate=0.25)
df_churn.to_csv('mobicash_churn_dataset.csv', index=False)

print(f"Generated {len(df_churn)} customer records")
print(f"Churn rate: {df_churn['churned'].mean():.1%}")
print(df_churn.head())