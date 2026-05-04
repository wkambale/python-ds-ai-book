# Daily transaction volume
daily_volume = df_time['amount_ugx'].resample('D').agg(['sum', 'count'])

daily_volume.columns = ['total_volume', 'num_transactions']