def create_daily_volume_plot(df: pd.DataFrame) -> None:
    """
    Creates a line plot of daily transaction volume.

    Args:
        df: DataFrame with datetime index and 'amount' column.
    """
    # Calculate daily volume
    daily_volume = df['amount'].resample('D').sum()

    # 1. Create a Figure and a single Axes object
    fig, ax = plt.subplots(figsize=(12, 6))

    # 2. Plot the data on the Axes
    ax.plot(
        daily_volume.index, 
        daily_volume.values, 
        color='#2E86AB', 
        linewidth=2,
        marker='o'
    )

    # 3. Add titles and labels
    ax.set_title('MobiCash Daily Transaction Volume', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume (UGX)')

    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 4. Adjust layout and display
    plt.tight_layout()
    plt.show()

create_daily_volume_plot(df_clean)