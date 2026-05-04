# Check missing values
print("Missing values per column:")
print(df.isnull().sum())

# Percentage of missing values
print("\nMissing percentage:")
print((df.isnull().sum() / len(df) * 100).round(1))