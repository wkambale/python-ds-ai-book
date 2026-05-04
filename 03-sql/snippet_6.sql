-- Count how many transactions of each type we have
-- "For each unique transaction_type, count the number of rows."
SELECT
    transaction_type,
    COUNT(*) AS number_of_transactions
FROM transactions
GROUP BY transaction_type;