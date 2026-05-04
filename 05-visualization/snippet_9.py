def plot_categorical_comparisons(df: pd.DataFrame) -> None:
    """
    Creates bar plots comparing amounts across categories.

    Args:
        df: DataFrame with transaction data.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Average amount by transaction type
    sns.barplot(
        data=df.reset_index(),
        x='transaction_type',
        y='amount',
        ax=axes[0],
        palette='Set2'
    )
    axes[0].set_title('Average Amount by Transaction Type')
    axes[0].set_xlabel('Transaction Type')
    axes[0].set_ylabel('Average Amount (UGX)')
    axes[0].tick_params(axis='x', rotation=45)

    # Right: Average amount by agent location
    sns.barplot(
        data=df.reset_index(),
        x='agent_location',
        y='amount',
        ax=axes[1],
        palette='Set2'
    )
    axes[1].set_title('Average Amount by Location')
    axes[1].set_xlabel('Agent Location')
    axes[1].set_ylabel('Average Amount (UGX)')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

plot_categorical_comparisons(df_clean)