# 1) CREATE TABLE
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# 2) INSERT rows
INSERT INTO orders (user_id, order_date, amount) VALUES
    (1, '2024-01-10', 150.00),
    (1, '2024-02-05', 90.00),
    (2, '2024-02-20', 220.00),
    (2, '2024-03-15', 45.00),
    (3, '2024-03-30', 110.00);

# 3) JOIN - vis users.name, orders.order_date og orders.amount
SELECT
    users.name,
    orders.order_date,
    orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;
