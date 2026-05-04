def plot_amount_distribution(df: pd.DataFrame) -> None:
    """
    Plots the distribution of transaction amounts with histogram and KDE.

    Args:
        df: DataFrame with 'amount' column.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Standard histogram with KDE
    sns.histplot(data=df, x='amount', bins=50, kde=True, ax=axes[0])
    axes[0].set_title('Distribution of Transaction Amounts')
    axes[0].set_xlabel('Amount (UGX)')
    axes[0].set_ylabel('Frequency')

    # Right: Log-transformed for better visibility of distribution shape
    sns.histplot(data=df, x='amount', bins=50, kde=True, ax=axes[1], log_scale=True)
    axes[1].set_title('Distribution (Log Scale)')
    axes[1].set_xlabel('Amount (UGX) - Log Scale')
    axes[1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.show()

    # Print summary statistics
    print(f"Median: {df['amount'].median():,.0f} UGX")
    print(f"Mean: {df['amount'].mean():,.0f} UGX")
    print(f"Skewness: {df['amount'].skew():.2f}")

plot_amount_distribution(df_clean)