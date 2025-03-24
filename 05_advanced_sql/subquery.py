# 1) Brugere med mindst én ordre over 100 (subquery i WHERE)
SELECT
    id, name, email
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
    WHERE amount > 100
);

# 2) (Valgfrit) Antal ordrer pr. bruger (subquery i SELECT)
SELECT
    id,
    name,
    (SELECT COUNT(*) FROM orders WHERE orders.user_id = users.id) AS ordre_antal
FROM users;
