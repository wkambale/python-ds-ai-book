# Strategy 1: Drop rows with any missing values
# Use sparingly - you lose data!
df_dropped = df.dropna()
print(f"Rows after dropna(): {len(df_dropped)} (lost {len(df) - len(df_dropped)} rows)")

# Strategy 2: Drop rows only if specific columns are missing
df_dropped_subset = df.dropna(subset=['customer_id', 'amount_ugx'])
print(f"Rows after dropna(subset=...): {len(df_dropped_subset)}")

# Strategy 3: Fill with a specific value
df_filled = df.copy()
df_filled['agent_location'] = df_filled['agent_location'].fillna('P2P Transfer')
df_filled['agent_id'] = df_filled['agent_id'].fillna('NO_AGENT')
print(f"\nAfter filling NaN values:")
print(df_filled['agent_location'].value_counts())

# Strategy 4: Fill with statistics (mean, median, mode)
# Useful for numeric columns
# df['amount_ugx'] = df['amount_ugx'].fillna(df['amount_ugx'].median())