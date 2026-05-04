def create_storytelling_plot(df: pd.DataFrame) -> None:
    """
    Creates a publication-ready plot demonstrating storytelling principles.

    Args:
        df: DataFrame with transaction data.
    """
    # Calculate daily volume
    daily_volume = df['amount'].resample('D').sum()

    # Find the peak day
    peak_day = daily_volume.idxmax()
    peak_value = daily_volume.max()

    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the line with subdued color
    ax.plot(daily_volume.index, daily_volume.values, color='lightgray', linewidth=2)
    
    # Highlight the peak
    ax.plot(peak_day, peak_value, marker='o', color='red', markersize=8)
    
    # Add an annotation explaining the peak
    ax.annotate(
        f"Peak Volume:\n{peak_value:,.0f} UGX\n(End of Month Salary)",
        xy=(peak_day, peak_value),
        xytext=(peak_day - pd.Timedelta(days=10), peak_value * 1.05),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9)
    )
    
    ax.set_title('Transaction Volume Spikes at Month-End', fontsize=16, fontweight='bold', loc='left')
    ax.set_xlabel('')
    ax.set_ylabel('Daily Volume (UGX)', color='gray')

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle=':', alpha=0.5)

    plt.tight_layout()
    plt.show()

create_storytelling_plot(df_clean)