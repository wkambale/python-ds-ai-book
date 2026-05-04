# Group by a single column
type_groups = df.groupby('transaction_type')
# Apply aggregate functions
print("Transaction type summary:")
print(type_groups['amount_ugx'].agg(['count', 'sum', 'mean', 'median']))