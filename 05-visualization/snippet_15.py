def create_interactive_dashboard(df: pd.DataFrame) -> None:
    """
    Creates a multi-panel interactive dashboard with Plotly.

    Args:
        df: DataFrame with transaction data.
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # Prepare aggregated data
    daily = df['amount'].resample('D').agg(['sum', 'count']).reset_index()
    daily.columns = ['date', 'volume', 'count']

    type_summary = df.groupby('transaction_type')['amount'].agg(['sum', 'mean', 'count']).reset_index()

    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Daily Volume', 'Daily Transaction Count', 'Volume by Type', 'Average Amount by Type'),
        specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "domain"}, {"type": "bar"}]]
    )

    # Add traces
    fig.add_trace(go.Scatter(x=daily['date'], y=daily['volume'], name='Volume'), row=1, col=1)
    fig.add_trace(go.Bar(x=daily['date'], y=daily['count'], name='Count'), row=1, col=2)
    fig.add_trace(go.Pie(labels=type_summary['transaction_type'], values=type_summary['sum'], name='Type Vol'), row=2, col=1)
    fig.add_trace(go.Bar(x=type_summary['transaction_type'], y=type_summary['mean'], name='Avg Amount'), row=2, col=2)

    fig.update_layout(
        height=700,
        title_text='MobiCash Transaction Dashboard',
        showlegend=False,
        template='plotly_white'
    )

    fig.show()

create_interactive_dashboard(df_clean)