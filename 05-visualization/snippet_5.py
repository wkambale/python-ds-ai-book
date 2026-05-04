def create_transaction_overview(df: pd.DataFrame) -> None:
    """
    Creates a 2x2 grid of overview plots for transaction data.

    Args:
        df: Cleaned MobiCash DataFrame.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('MobiCash Transaction Overview', fontsize=14, fontweight='bold')

    # Plot 1: Daily volume (top-left)
    daily_volume = df['amount'].resample('D').sum()
    axes[0, 0].plot(daily_volume.index, daily_volume.values, color='#2E86AB')
    axes[0, 0].set_title('Daily Transaction Volume')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Volume (UGX)')
    axes[0, 0].tick_params(axis='x', rotation=45)

    # Plot 2: Average amount by type (top-right)
    avg_by_type = df.groupby('transaction_type')['amount'].mean().sort_values()
    axes[0, 1].barh(avg_by_type.index, avg_by_type.values, color='#A23B72')
    axes[0, 1].set_title('Average Amount by Type')
    axes[0, 1].set_xlabel('Amount (UGX)')

    # Plot 3: Transaction counts by location (bottom-left)
    loc_counts = df['agent_location'].value_counts()
    axes[1, 0].bar(loc_counts.index, loc_counts.values, color='#F18F01')
    axes[1, 0].set_title('Transactions by Agent Location')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].tick_params(axis='x', rotation=45)

    # Plot 4: Amount distribution (bottom-right)
    axes[1, 1].hist(df['amount'], bins=30, color='#39A9DB', edgecolor='black')
    axes[1, 1].set_title('Amount Distribution')
    axes[1, 1].set_xlabel('Amount (UGX)')
    axes[1, 1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()

create_transaction_overview(df_clean)