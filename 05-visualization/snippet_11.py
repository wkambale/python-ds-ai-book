def plot_hour_vs_amount(df: pd.DataFrame, sample_size: int = 500) -> None:
    """
    Creates a scatter plot of transaction amount vs. hour of day.

    Args:
        df: DataFrame with 'hour_of_day' and 'amount' columns.
        sample_size: Number of points to plot (for readability).
    """
    # Sample for readability if dataset is large
    plot_data = df.sample(min(sample_size, len(df)), random_state=42).reset_index()

    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=plot_data,
        x='hour_of_day',
        y='amount',
        hue='transaction_type',
        alpha=0.6,
        s=60
    )
    plt.title('Transaction Amount vs. Hour of Day')
    plt.xlabel('Hour of Day (0-23)')
    plt.ylabel('Amount (UGX)')
    plt.legend(title='Transaction Type', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

plot_hour_vs_amount(df_clean)