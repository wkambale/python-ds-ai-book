-- Find all transactions that were deposits
SELECT *
FROM transactions
WHERE transaction_type = 'deposit';

-- Find all transactions with an amount greater than 2000 KES
SELECT *
FROM transactions
WHERE amount_kes > 2000;