# Single column (returns a Series)
amounts = df['amount_ugx']
print(f"Type: {type(amounts)}")

# Multiple columns (returns a DataFrame)
subset = df[['customer_id', 'amount_ugx', 'transaction_type']]
print(f"Type: {type(subset)}")

# Dot notation (only works for column names without spaces/special characters)
# Not recommended for production code as it can conflict with methods
amounts_dot = df.amount_ugx