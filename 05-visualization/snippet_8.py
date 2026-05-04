def plot_amount_boxplots(df: pd.DataFrame) -> None:
    """
    Creates box plots of transaction amounts, overall and by type.

    Args:
        df: DataFrame with 'amount' and 'transaction_type' columns.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Overall distribution
    sns.boxplot(y=df['amount'], ax=axes[0], color='#2E86AB')
    axes[0].set_title('Overall Amount Distribution')
    axes[0].set_ylabel('Amount (UGX)')

    # Right: By transaction type
    sns.boxplot(data=df.reset_index(), x='transaction_type', y='amount', ax=axes[1])
    axes[1].set_title('Amount Distribution by Transaction Type')
    axes[1].set_xlabel('Transaction Type')
    axes[1].set_ylabel('Amount (UGX)')

    plt.tight_layout()
    plt.show()

plot_amount_boxplots(df_clean)