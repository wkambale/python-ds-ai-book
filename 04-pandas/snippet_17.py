# Demonstrate type conversion issues
messy_amounts = pd.Series(['50000', '25,000', '10000 UGX', 'invalid', '75000'])
print("Messy data:")
print(messy_amounts)

# pd.to_numeric with errors='coerce' converts invalid values to NaN
numeric_amounts = pd.to_numeric(
    messy_amounts.str.replace(',', '').str.replace(' UGX', ''),
    errors='coerce'
)
print("\nAfter conversion:")
print(numeric_amounts)

# Check which values failed conversion
failed_mask = numeric_amounts.isnull() & messy_amounts.notna()
print(f"\nFailed conversions: {messy_amounts[failed_mask].tolist()}")