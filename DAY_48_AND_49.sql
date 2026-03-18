create database student_db;
use student_db;

create table students (
    std_id int primary key,
    name varchar(50),
    age int,
    city varchar(50),
    course_id int
);

insert into students (std_id, name, age, city, course_id) values
(1, 'alice', 21, 'london', 101),
(2, 'bob', 22, 'paris', 102),
(3, 'charlie', 20, 'london', 103),
(4, 'david', 23, 'berlin', 101),
(5, 'emma', 21, 'paris', 104),
(6, 'frank', 22, 'london', 105),
(7, 'grace', 20, 'rome', 102),
(8, 'henry', 24, 'paris', 103),
(9, 'isabella', 21, 'london', 104),
(10, 'jack', 22, 'madrid', 105);

create table courses (
    course_id int primary key,
    course_name varchar(50),
    fees int not null,
    instructor varchar(50)
);

insert into courses (course_id, course_name, fees, instructor) values
(101, 'python programming', 800, 'dr. smith'),
(102, 'data structures', 1200, 'prof. johnson'),
(103, 'database systems', 1500, 'dr. brown'),
(104, 'machine learning', 2000, 'dr. taylor'),
(105, 'web development', 700, 'prof. davis');

-- show all student names who live in london or paris
select name from students 
where city in ('london', 'paris');

-- list all courses where fees are between 500 and 1500
select * from courses 
where fees between 500 and 1500;

-- show students’ names and cities ordered alphabetically
select name, city from students 
order by name asc;

-- find the average fees of all courses
select avg(fees) as average_fees 
from courses;

-- list the total number of students enrolled in each course_id
select course_id, count(std_id) as total_students 
from students 
group by course_id;

-- display student name and their course name (join)
select s.name, c.course_name
from students s
join courses c
on s.course_id = c.course_id;

-- cities with more than 20 students (sorted by count descending)
select city, count(std_id) as total_students
from students
group by city
having count(std_id) > 20
order by total_students desc;

-- display student details with course names
select s.std_id, s.name, c.course_name
from students s
join courses c
on s.course_id = c.course_id;

-- calculate total fees collected for each course
select c.course_name, sum(c.fees) as total_fees
from students s
join courses c
on s.course_id = c.course_id
group by c.course_name;