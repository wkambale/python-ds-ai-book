# Using pd.cut for binning numeric values into categories
df_eng['amount_category'] = pd.cut(
    df_eng['amount_ugx'],
    bins=[0, 20000, 100000, float('inf')],
    labels=['Small', 'Medium', 'Large'],
    right=False
)

print(df_eng['amount_category'].value_counts())