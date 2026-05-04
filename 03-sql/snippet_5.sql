-- Get the 5 most recent transactions
SELECT *
FROM transactions
ORDER BY transaction_date DESC
LIMIT 5;

-- Preview the first 10 rows of a large table
SELECT *
FROM customers
LIMIT 10;