-- "Find customers who made a purchase but never contacted support"
SELECT DISTINCT c.customer_id, c.name
FROM customers c
INNER JOIN purchases p ON c.customer_id = p.customer_id
LEFT JOIN support_tickets s ON c.customer_id = s.customer_id
WHERE s.ticket_id IS NULL;