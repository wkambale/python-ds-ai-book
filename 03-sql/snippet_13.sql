SELECT COUNT(*) FROM transactions WHERE agent_id IS NULL;

a) The number of transactions with an agent +
b) The number of transactions without an agent +
c) The total of all agent_id values +
d) An error, because you cannot use IS NULL with COUNT +