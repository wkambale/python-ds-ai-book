-- List all customers and their transaction count
-- Include customers who have made zero transactions
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(t.transaction_id) AS num_transactions,
    COALESCE(SUM(t.amount_kes), 0) AS total_volume
FROM customers AS c
LEFT JOIN transactions AS t
    ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_volume DESC;