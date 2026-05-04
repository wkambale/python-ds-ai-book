-- Find all withdrawals that were greater than 1000 KES
SELECT *
FROM transactions
WHERE transaction_type = 'withdrawal' AND amount_kes > 1000;

-- Find all transactions that were either deposits or transfers
SELECT *
FROM transactions
WHERE transaction_type IN ('deposit', 'transfer');

-- Find transactions between 1000 and 5000 KES (inclusive)
SELECT *
FROM transactions
WHERE amount_kes BETWEEN 1000 AND 5000;

-- Find any agent whose name contains the word 'Kiosk'
-- The '%' is a wildcard for "any sequence of characters"
SELECT *
FROM agents
WHERE agent_name LIKE '%Kiosk%';

-- Find transactions that did not happen at an agent (e.g., a peer-to-peer transfer)
SELECT *
FROM transactions
WHERE agent_id IS NULL;