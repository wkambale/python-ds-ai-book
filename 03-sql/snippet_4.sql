-- Get all transactions, ordered from the largest amount to the smallest
SELECT *
FROM transactions
ORDER BY amount_kes DESC;

-- Get all customers, ordered alphabetically by their last name
SELECT *
FROM customers
ORDER BY last_name ASC;  -- ASC is the default, so it's optional

-- Sort by multiple columns: first by type, then by amount within each type
SELECT *
FROM transactions
ORDER BY transaction_type ASC, amount_kes DESC;