def categorize_transaction(amount: float) -> str:
    """Categorize transaction by amount tier."""
    if amount < 20000:
        return 'Small'
    elif amount < 100000:
        return 'Medium'
    else:
        return 'Large'

# Apply to a single column
df_eng['amount_category'] = df_eng['amount_ugx'].apply(categorize_transaction)

print(df_eng['amount_category'].value_counts())