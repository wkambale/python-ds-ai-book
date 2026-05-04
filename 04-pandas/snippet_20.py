# Work with a clean copy
df_eng = df.copy()

# Method 1: Direct assignment
df_eng['amount_usd'] = df_eng['amount_ugx'] / 3700  # Approximate exchange rate

# Method 2: Conditional assignment with np.where
df_eng['transaction_fee'] = np.where(
    df_eng['transaction_type'] == 'withdrawal',
    df_eng['amount_ugx'] * 0.01,  # 1% fee for withdrawals
    0  # No fee otherwise
)

# Method 3: Using .loc for conditional assignment
df_eng['is_high_value'] = False
df_eng.loc[df_eng['amount_ugx'] > 100000, 'is_high_value'] = True

print(df_eng[['transaction_type', 'amount_ugx', 'amount_usd',
              'transaction_fee', 'is_high_value']].head(10))