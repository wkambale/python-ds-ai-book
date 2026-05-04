print("\nTransaction Types")
print(df['transaction_type'].value_counts())

print("\nAgent Locations (excluding NaN)")
print(df['agent_location'].value_counts())

print("\nMissing Values by Column")
print(df.isnull().sum())