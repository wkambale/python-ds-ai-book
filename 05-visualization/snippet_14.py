import plotly.express as px

def create_interactive_scatter(df: pd.DataFrame) -> None:
    """
    Creates an interactive scatter plot with Plotly.

    Args:
        df: DataFrame with transaction data.
    """
    # Prepare data (reset index for Plotly)
    plot_data = df.reset_index().sample(min(500, len(df)), random_state=42)

    # Create interactive scatter plot
    fig = px.scatter(
        plot_data,
        x='hour_of_day',
        y='amount',
        color='transaction_type',
        size='amount',
        hover_data=['transaction_id', 'agent_location'],
        title='Interactive Transaction Explorer',
        labels={
            'hour_of_day': 'Hour of Day',
            'amount': 'Transaction Amount (UGX)',
            'transaction_type': 'Type'
        }
    )
    
    fig.update_layout(
        template='plotly_white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )

    fig.show()

create_interactive_scatter(df_clean)