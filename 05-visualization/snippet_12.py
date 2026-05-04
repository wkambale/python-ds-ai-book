def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Creates a correlation heatmap for numeric variables.

    Args:
        df: DataFrame with numeric columns.
    """
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    correlation_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap='RdBu_r',
        center=0,
        fmt='.2f',
        square=True,
        linewidths=0.5
    )
    plt.title('Correlation Matrix of Numeric Features')
    plt.tight_layout()
    plt.show()

plot_correlation_heatmap(df_clean)