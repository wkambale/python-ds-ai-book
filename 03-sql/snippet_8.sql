-- Find customers whose total transaction volume exceeds 5000 KES
SELECT
    customer_id,
    SUM(amount_kes) AS total_volume,
    COUNT(*) AS num_transactions
FROM transactions
GROUP BY customer_id
HAVING SUM(amount_kes) > 5000
ORDER BY total_volume DESC;