# Equivalent to the boolean mask approach, but more readable
result = df.query("transaction_type == 'deposit' and amount_ugx > 50000")
print(f"High-value deposits (using query): {len(result)}")
# You can reference variables with @
min_amount = 75000
result = df.query("amount_ugx >= @min_amount")
print(f"Transactions >= {min_amount}: {len(result)}")