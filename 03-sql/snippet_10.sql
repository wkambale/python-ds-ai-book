SELECT
    t.transaction_id,
    t.amount_kes,
    t.transaction_date,
    c.first_name,
    c.last_name
FROM transactions AS t
INNER JOIN customers AS c
    ON t.customer_id = c.customer_id;