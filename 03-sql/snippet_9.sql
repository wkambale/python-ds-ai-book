-- Find customers with more than 3000 KES in deposits only
SELECT
    customer_id,
    SUM(amount_kes) AS total_deposits
FROM transactions
WHERE transaction_type = 'deposit'  -- Filter rows BEFORE grouping
GROUP BY customer_id
HAVING SUM(amount_kes) > 3000       -- Filter groups AFTER aggregation
ORDER BY total_deposits DESC;