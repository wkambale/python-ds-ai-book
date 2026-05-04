# Calculate 7-day rolling average of daily volume
daily_volume = df_time['amount_ugx'].resample('D').sum()
rolling_avg = daily_volume.rolling(window=7).mean()
print("7-day rolling average (showing days 7-14):")
print(rolling_avg.iloc[6:14].round(0))