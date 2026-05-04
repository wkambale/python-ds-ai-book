# Create messy location data for demonstration
messy_locations = pd.Series(['  kampala ', 'Nairobi West', 'KAMPALA', ' nairobi  '])
print("Messy locations:")
print(messy_locations.tolist())

# Chain string methods to clean
clean_locations = (messy_locations
    .str.strip()           # Remove leading/trailing whitespace
    .str.lower()           # Convert to lowercase
    .str.replace(' west', '', regex=False)  # Remove suffixes
    .str.title()           # Convert to title case
)
print("\nCleaned locations:")
print(clean_locations.tolist())