-- "Calculate running total of sales and rank salespeople by monthly performance"
SELECT
    salesperson_id,
    sale_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY salesperson_id
        ORDER BY sale_date
    ) as running_total,
    RANK() OVER (
        PARTITION BY DATE_TRUNC('month', sale_date)
        ORDER BY SUM(amount) DESC
    ) as monthly_rank
FROM sales;