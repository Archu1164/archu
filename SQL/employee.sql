CREATE DATABASE Employee;
USE Employee;

CREATE TABLE Employee(
Employee_id INT PRIMARY KEY,
name VARCHAR(30),
department VARCHAR(30),
salary INT,
joined_date DATE
);

INSERT INTO employee(name,department,salary,joined_date)VALUES
('Archana','IT',30000,'2025-12-30'),
('Ramana','HR',60000,'2023-10-20'),
('priya','IT',35000,'2024-08-01'),
('Pri','IT',26000,'2025-11-17'),
('Bhodi','Finance',28000,'2024-09-21');


