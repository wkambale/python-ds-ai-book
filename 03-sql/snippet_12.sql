-- Get a complete view of each transaction with customer and agent names
SELECT
    t.transaction_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    a.agent_name,
    a.location AS agent_location,
    t.transaction_type,
    t.amount_kes,
    t.transaction_date
FROM transactions AS t
INNER JOIN customers AS c
    ON t.customer_id = c.customer_id
LEFT JOIN agents AS a
    ON t.agent_id = a.agent_id
ORDER BY t.transaction_date DESC;