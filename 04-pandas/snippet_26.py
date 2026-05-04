filtered = df.groupby('transaction_type').filter(lambda x: len(x) > 15)
print(f"Original rows: {len(df)}, After filter: {len(filtered)}")
print(f"Remaining types: {filtered['transaction_type'].unique().tolist()}")