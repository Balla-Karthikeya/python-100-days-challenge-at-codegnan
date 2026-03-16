-- select database 
use it_companyy;

-- check tables
use it_company;
show tables;

-- check dept table data and employee data 
select *from dept;

select *from employee;

insert into employee(name, dept_id, salary) values('karthik', 1004, 10000);

--  inner join 
-- select empid, name and deptname from dept and employee tables 
select emp_id, name, dept_name from dept 
inner join employee
on dept.dept_id  =  employee.DEPT_ID;

select emp_id, name, dept_name from dept 
inner join employee
on dept.dept_id  =  employee.DEPT_ID
where dept_name = 'it';

select dept_name, count(*) from dept
inner join employee
on dept.dept_id = employee.dept_id
group by dept_name;

 -- left join
 select emp_id, name, dept_name from dept 
left join employee
on dept.dept_id  =  employee.DEPT_ID;
 
 -- create dept table 
 create table dept01(
        id int,
        name varchar(20),
        location varchar(20) default 'INDIA'
);

-- insert data into dept1 table
insert into dept01(id, name, location)
values(1001,'it','usa'), (1002,'sales','uae');


insert into dept01(id,name,location)
values (1004,'hr'), (1005,'marketing');

 -- left join
 select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID;


-- right join
 select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID;


-- full join 
(select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID)
union
(select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID);

(select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID)
union all
(select id, dept01.name, EMP_ID, employee.name from dept01 
left join employee
on dept01.id  =  employee.DEPT_ID);




