# Select first row (position 0)
first_row = df_indexed.iloc[0]
print("First row:")
print(first_row)

# Select rows 0-4 and columns 0-2
subset = df_indexed.iloc[0:5, 0:3]
print("\nFirst 5 rows, first 3 columns:")
print(subset)

# Select specific positions (non-contiguous)
specific = df_indexed.iloc[[0, 5, 10], [0, 2]]
print("\nSpecific positions:")
print(specific)