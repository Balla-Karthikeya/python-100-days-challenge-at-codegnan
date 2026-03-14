SHOW DATABASES;

USE it_company;

SHOW TABLES;

SELECT COUNT(EMP_ID)
FROM EMPLOYEE;

-- FIND THE IT DEPT EMPLOYEE COUNT 
SELECT COUNT(EMP_ID) AS IT_Employee_Count
FROM EMPLOYEE
WHERE DEPT_ID = 1001;


-- FIND SALES DEPT EMPLOYEE  COUNT 
SELECT COUNT(EMP_ID) AS Sales_Employee_Count
FROM EMPLOYEE
WHERE DEPT_ID = 1002;


-- FIND HR DEPT EMPLOYEE COUNT 
SELECT COUNT(EMP_ID) AS HR_Employee_Count
FROM EMPLOYEE
WHERE DEPT_ID = 1003;

SELECT dept_id, COUNT(*) AS emp_count FROM employee
GROUP BY dept_id;

-- find 1001 and 1002 depts employee count 
SELECT dept_id, COUNT(*)  as count, sum(salary) from employee
where dept_id in (1001, 1002)
group by dept_id;

-- Find maximum salary in each department
SELECT DEPT_ID, MAX(SALARY) AS MAX_SALARY
FROM EMPLOYEE
GROUP BY DEPT_ID;

-- Find minimum salary in each department
SELECT DEPT_ID, MIN(SALARY) AS MIN_SALARY
FROM EMPLOYEE
GROUP BY DEPT_ID;

-- Find average salary company spends on each department
SELECT DEPT_ID, AVG(SALARY) AS AVG_SALARY
FROM EMPLOYEE
GROUP BY DEPT_ID;

-- Return 1001 and 1002 department minimum salary
SELECT DEPT_ID, MIN(SALARY) AS MIN_SALARY
FROM EMPLOYEE
WHERE DEPT_ID IN (1001,1002)
GROUP BY DEPT_ID;

-- Return all departments total employees
SELECT DEPT_ID, COUNT(*) AS TOTAL_EMPLOYEES
FROM EMPLOYEE
GROUP BY DEPT_ID;