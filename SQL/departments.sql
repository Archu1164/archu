CREATE DATABASE employee_org;
USE employee_org;

CREATE DEPARTMENTS table (without foreign keys)
CREATE TABLE DEPARTMENTS(
dept_id INT_INCREMENT PRIMARY KEY,
dept_name VARCHAR(50) NOT NULL UNIQUE,
location VARCHAR(100) NOT NULL,
budget DECIMAL(15,2) DEFAULT 0,
manager_id INT,
created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

CONSTRAINT chk_dept_budget CHECK(budget >=0));
