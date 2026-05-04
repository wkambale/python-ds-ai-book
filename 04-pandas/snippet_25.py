# Group by location and transaction type
grouped = df.groupby(['agent_location', 'transaction_type'])
# Use .agg() with a dictionary for different aggregations per column
summary = grouped.agg(
    total_volume=('amount_ugx', 'sum'),
    num_transactions=('transaction_id', 'count'),
    unique_customers=('customer_id', 'nunique'),
    avg_amount=('amount_ugx', 'mean')

).round(0)