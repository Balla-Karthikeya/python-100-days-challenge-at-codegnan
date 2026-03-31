-- 1. Create Database
CREATE DATABASE CompanyDB;
USE CompanyDB;

-- 2. Create Departments Table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

-- 3. Create Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- 4. Insert Sample Data into Departments
INSERT INTO Departments VALUES
(1, 'IT', 'Hyderabad'),
(2, 'HR', 'Mumbai'),
(3, 'Finance', 'Delhi'),
(4, 'Marketing', 'Bangalore');

-- 5. Insert Sample Data into Employees
INSERT INTO Employees VALUES
(101, 'Karthik', 1, 60000),
(102, 'Ravi', 2, 40000),
(103, 'Anjali', 1, 70000),
(104, 'Priya', 3, 55000),
(105, 'Rahul', 4, 30000),
(106, 'Sneha', 2, 52000);

--------------------------------------------------
-- 6. Query 11: Employees earning more than average salary
SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

--------------------------------------------------
-- 7. Query 12: Departments with employees having salary > 50000
SELECT DISTINCT d.dept_id, d.dept_name
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
WHERE e.salary > 50000;

--------------------------------------------------
-- 8. Query 13: List all employees with their department name
SELECT e.emp_id, e.emp_name, e.salary, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;

--------------------------------------------------
-- 9. Query 14: Show all departments and employees (including empty)
SELECT d.dept_id, d.dept_name, e.emp_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id;

--------------------------------------------------
-- 10. Query 15: Employees working in IT department
SELECT e.emp_id, e.emp_name, e.salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';