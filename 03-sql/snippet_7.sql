-- Find the total amount transacted by each customer
SELECT
    customer_id,
    SUM(amount_kes) AS total_volume,
    AVG(amount_kes) AS average_transaction_size,
    COUNT(*) AS number_of_transactions,
    MIN(transaction_date) AS first_transaction,
    MAX(transaction_date) AS last_transaction
FROM transactions
GROUP BY customer_id
ORDER BY total_volume DESC;