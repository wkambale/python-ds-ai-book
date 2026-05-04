def plot_temporal_patterns(df: pd.DataFrame) -> None:
    """
    Creates visualizations of temporal patterns in transaction data.

    Args:
        df: DataFrame with datetime index.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top-left: Daily volume over time
    daily_volume = df['amount'].resample('D').sum()
    axes[0, 0].plot(daily_volume.index, daily_volume.values, marker='o', markersize=3)
    axes[0, 0].set_title('Daily Transaction Volume')
    axes[0, 0].set_ylabel('Total Volume (UGX)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Top-right: Moving average
    daily_volume.plot(alpha=0.3, color='gray', ax=axes[0, 1], label='Daily')
    daily_volume.rolling(window=7).mean().plot(color='red', linewidth=2, ax=axes[0, 1], label='7-Day MA')
    axes[0, 1].set_title('7-Day Moving Average')
    axes[0, 1].legend()
    axes[0, 1].tick_params(axis='x', rotation=45)

    # Bottom-left: Day of week patterns
    sns.boxplot(data=df, x='day_of_week', y='amount', ax=axes[1, 0])
    axes[1, 0].set_title('Transaction Amounts by Day of Week')
    axes[1, 0].tick_params(axis='x', rotation=45)

    # Bottom-right: Heatmap of day vs hour
    pivot = pd.crosstab(df['day_of_week'], df['hour_of_day'])
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(day_order)
    sns.heatmap(pivot, cmap='YlOrRd', ax=axes[1, 1], cbar_kws={'label': 'Transactions'})
    axes[1, 1].set_title('Transaction Frequency: Day vs. Hour')
    axes[1, 1].set_xlabel('Hour of Day')
    axes[1, 1].set_ylabel('Day of Week')

    plt.tight_layout()
    plt.show()

plot_temporal_patterns(df_clean)