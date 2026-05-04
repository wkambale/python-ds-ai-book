is_deposit = df['transaction_type'] == 'deposit'
is_high_value = df['amount_ugx'] > 50000

print("Boolean mask (first 5 values):")
print(is_deposit.head())

# Use the mask to filter
deposits = df[is_deposit]
print(f"\nNumber of deposits: {len(deposits)}")

# Combine masks with logical operators
# & for AND, | for OR, ~ for NOT
# IMPORTANT: Use parentheses around each condition!
high_value_deposits = df[(is_deposit) & (is_high_value)]
print(f"High-value deposits: {len(high_value_deposits)}")

# More complex example: High-value deposits in Kampala
is_kampala = df['agent_location'] == 'Kampala'
result = df[(is_deposit) & (is_high_value) & (is_kampala)]
print(f"\nHigh-value Kampala deposits:")
print(result[['customer_id', 'amount_ugx', 'agent_location']])