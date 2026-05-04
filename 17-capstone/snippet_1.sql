-- "Find the top 5 customers by total transaction value this month"
SELECT
    customer_id,
    SUM(amount) as total_value
FROM transactions
WHERE transaction_date >= DATE_TRUNC('month', CURRENT_DATE)
GROUP BY customer_id
ORDER BY total_value DESC
LIMIT 5;