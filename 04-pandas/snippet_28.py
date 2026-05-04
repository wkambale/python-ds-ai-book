# Set timestamp as the index
df_time = df.copy()
df_time = df_time.set_index('timestamp').sort_index()
# Select data with partial string indexing
jan_data = df_time.loc['2025-01']
print(f"January transactions: {len(jan_data)}")
# Select a specific date

jan_20 = df_time.loc['2025-01-20']