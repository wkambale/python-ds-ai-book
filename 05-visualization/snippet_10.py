def plot_transaction_counts(df: pd.DataFrame) -> None:
    """
    Creates count plots showing transaction frequency by category.

    Args:
        df: DataFrame with transaction data.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: By transaction type
    sns.countplot(
        data=df.reset_index(),
        x='transaction_type',
        ax=axes[0],
        palette='Set2'
    )
    axes[0].set_title('Number of Transactions by Type')
    axes[0].set_xlabel('Transaction Type')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    # Right: By agent location
    sns.countplot(
        data=df.reset_index(),
        x='agent_location',
        ax=axes[1],
        palette='Set2'
    )
    axes[1].set_title('Number of Transactions by Location')
    axes[1].set_xlabel('Count')
    axes[1].set_ylabel('Agent Location')

    plt.tight_layout()
    plt.show()

plot_transaction_counts(df_clean)