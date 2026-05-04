# Extract datetime components
df_eng['date'] = df_eng['timestamp'].dt.date
df_eng['hour'] = df_eng['timestamp'].dt.hour
df_eng['day_of_week'] = df_eng['timestamp'].dt.day_name()
df_eng['is_weekend'] = df_eng['timestamp'].dt.dayofweek >= 5

print(df_eng[['timestamp', 'date', 'hour', 'day_of_week', 'is_weekend']].head())