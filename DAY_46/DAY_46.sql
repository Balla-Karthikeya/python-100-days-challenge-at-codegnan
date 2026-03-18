use it_company;
show tables;

select *from employee;

SELECT UPPER(name) FROM employee;

SELECT LOWER(name) from employee;

SELECT LPAD(name, 10, ' ' )FROM employee; 

SELECT RPAD(name, 10, ' ' )FROM employee;

select trim(name) from employee;

SELECT CONCAT(name, ' works in ', dept_id) 
FROM employee;

SELECT CURDATE();

SELECT CURTIME();

select date_format("2024-12-25","%d/%m/%y");

select day(date(now()));

SELECT ABS(-10);

SELECT SQRT(9);

SELECT POW(3, 2);