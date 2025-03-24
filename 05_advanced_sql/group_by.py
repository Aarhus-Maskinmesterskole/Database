# Vis summen af orders.amount pr. bruger
# og filtrér kun dem med samlet beløb over 100

SELECT
    users.name,
    SUM(orders.amount) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.name
HAVING SUM(orders.amount) > 100;
