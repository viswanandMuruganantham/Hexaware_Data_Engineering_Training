CREATE DATABASE expense_monitoring_system;
USE expense_monitoring_system;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) UNIQUE
);

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    expense_date DATE,
    description VARCHAR(255),

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);



INSERT INTO users(full_name, email, phone)
VALUES
('Viswanand', 'viswa@gmail.com', '9876543210'),
('Arun', 'arun@gmail.com', '9123456780');


INSERT INTO categories(category_name)
VALUES
('Food'),
('Transport'),
('Shopping'),
('Bills'),
('Entertainment');



INSERT INTO expenses(user_id, category_id, amount, expense_date, description)
VALUES
(1, 1, 250.00, '2026-05-01', 'Lunch'),
(1, 2, 100.00, '2026-05-02', 'Bus Fare'),
(1, 3, 2000.00, '2026-05-03', 'New Shoes'),
(2, 1, 500.00, '2026-05-01', 'Dinner');


INSERT INTO expenses(user_id, category_id, amount, expense_date, description)
VALUES
(1, 4, 1500.00, '2026-05-05', 'Electricity Bill');



SELECT
e.expense_id,
u.full_name,
c.category_name,
e.amount,
e.expense_date,
e.description
FROM expenses e
JOIN users u ON e.user_id = u.user_id
JOIN categories c ON e.category_id = c.category_id;



UPDATE expenses
SET amount = 1800
WHERE expense_id = 4;

DELETE FROM expenses
WHERE expense_id = 4;


DELIMITER $$

CREATE PROCEDURE GetMonthlyCategoryExpense(
    IN input_month INT,
    IN input_year INT
)
BEGIN
    SELECT
        c.category_name,
        SUM(e.amount) AS total_expense
    FROM expenses e
    JOIN categories c
        ON e.category_id = c.category_id
    WHERE MONTH(e.expense_date) = input_month
      AND YEAR(e.expense_date) = input_year
    GROUP BY c.category_name;
END $$

DELIMITER ;

CALL GetMonthlyCategoryExpense(5, 2026);