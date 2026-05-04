# Select a single row by its label
row = df_indexed.loc['TXN001']
print("Single row:")
print(row)

# Select multiple rows by labels
rows = df_indexed.loc[['TXN001', 'TXN002', 'TXN003']]
print("\nMultiple rows:")
print(rows)

# Select rows and specific columns
subset = df_indexed.loc['TXN001':'TXN005', ['customer_id', 'amount_ugx']]
print("\nRows and columns:")
print(subset)