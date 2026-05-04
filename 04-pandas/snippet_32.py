customers = pd.DataFrame({

    'customer_id': ['CUS101', 'CUS102', 'CUS103', 'CUS104', 'CUS105'],
    'customer_name': ['Ade Bello', 'Wanjiru Kamau', 'Kwesi Mensah',
                      'Amina Diallo', 'Kofi Asante'],
    'join_date': pd.to_datetime(['2024-03-15', '2023-11-20', '2024-01-05',
                                  '2024-06-01', '2024-02-10'])
})

merged_df = pd.merge(
    df,
    customers,
    on='customer_id',
    how='inner'
)
print("Merged data sample:")
print(merged_df[['transaction_id', 'customer_id', 'customer_name', 'amount_ugx']].head())