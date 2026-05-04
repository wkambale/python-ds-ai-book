# Add each customer's average transaction amount as a new column

df_eng['customer_avg_amount'] = df_eng.groupby('customer_id')['amount_ugx'].transform('mean')

df_eng['amount_vs_avg'] = df_eng['amount_ugx'] - df_eng['customer_avg_amount']