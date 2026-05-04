SELECT customer_id, first_name, SUM(amount)
FROM transactions
INNER JOIN customers ON transactions.customer_id = customers.customer_id
GROUP BY customer_id;

a) You cannot use INNER JOIN with GROUP BY +
b) The SUM function requires an alias +
c) `first_name` is not in the GROUP BY clause (required in most databases) +
d) The ON clause syntax is incorrect +