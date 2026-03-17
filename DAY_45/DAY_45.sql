use it_companyy;
show tables;

-- check tables
use it_company;
show tables;

select *from employee;

--  return the ram's dept employee details
select dept_id from employee 
where name = "Ram";

select *from employee
where dept_id = 1001;

select *from employee
where dept_id = (select dept_id from employee where name = 'Ram');

-- return employee those salary morethan the average salary of employees 
select *from employee 
where salary > (select avg(salary)  from employee);

-- return the ram's dept employee details without ram's details 
select *from employee
where dept_id = (select dept_id from employee where name = 'Ram') and name != 'ram';

-- return employee details whose salary is greater than the 1001 dept's minimum salary 
select *from employee 
where salary = (select min(salary) from employee where dept_id = 1001);

-- return employee details whose salary is grater than the  any one of 1001 dept employee salary
select *from employee 
where salary > any(select salary from employee where dept_id  = 1002);

-- return employee details whose salary is lesser than the all 1002's dept employees salary 
select *from employee 
where salary > all(select salary from employee where dept_id  = 1001);

-- return employee names those not belongs to 1003 dept 
select *from employee 
where name not in (select name from employee where dept_id = 1003);



