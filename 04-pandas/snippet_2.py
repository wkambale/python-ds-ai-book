import pandas as pd

# A Series is a single column with an index
transaction_amounts = pd.Series(
    [50000, 25000, 10000],
    index=['TXN001', 'TXN002', 'TXN003'],
    name='amount_ugx'
)
print("Series example:")
print(transaction_amounts)
print(f"\nIndex: {transaction_amounts.index.tolist()}")
print(f"Values: {transaction_amounts.values.tolist()}")