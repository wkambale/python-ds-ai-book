# Check for fully duplicate rows
print(f"Fully duplicate rows: {df.duplicated().sum()}")

# Check for duplicates based on specific columns
# (same customer, amount, and timestamp might indicate a duplicate entry)
duplicate_mask = df.duplicated(subset=['customer_id', 'amount_ugx', 'timestamp'])
print(f"Potential duplicate transactions: {duplicate_mask.sum()}")

# View the duplicates
if duplicate_mask.sum() > 0:
    print(df[duplicate_mask])

# Remove duplicates (keep first occurrence)
df_unique = df.drop_duplicates(subset=['customer_id', 'amount_ugx', 'timestamp'])
print(f"Rows after deduplication: {len(df_unique)}")