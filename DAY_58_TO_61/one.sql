-- CREATE TABLES
-- Create Classes Table
CREATE TABLE classes (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50)
);

-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    class_id INT,
    marks INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- INSERT DATA
-- Insert into classes table
INSERT INTO classes VALUES
(1, 'CSE'),
(2, 'ECE'),
(3, 'MECH');

-- Insert into students table
INSERT INTO students VALUES
(101, 'Ravi', 1, 85),
(102, 'Anita', 1, 90),
(103, 'Suresh', 2, 78),
(104, 'Kiran', 2, 88),
(105, 'Manoj', 3, 70);


-- PART B – QUERY BASED
-- Q1: Write an SQL query to display all records from the classes table
SELECT * FROM classes;

-- Q2: Write an SQL query to display class names in uppercase
SELECT UPPER(class_name) AS class_name FROM classes;

-- Q3: Write an SQL query to display class names in uppercase using a function
SELECT UPPER(class_name) FROM classes;

-- Q4: Write an SQL query to display length of each class name using a function
SELECT class_name, LENGTH(class_name) AS name_length FROM classes;

-- Q5: Write an SQL query to display class name and its first three characters
SELECT class_name, SUBSTRING(class_name, 1, 3) AS short_name FROM classes;

-- Q6: Write an SQL query to count the total number of classes
SELECT COUNT(*) AS total_classes FROM classes;



-- PART C – QUERY BASED
-- Q1: Write an SQL query to find the total number of students in each class
SELECT class_id, COUNT(*) AS total_students
FROM students
GROUP BY class_id;

-- Q2: Write an SQL query to find the average marks obtained in each class (rounded to 2 decimals)
SELECT class_id, ROUND(AVG(marks), 2) AS avg_marks
FROM students
GROUP BY class_id;

-- Q3: Write an SQL query to find the highest and lowest marks in each class
SELECT class_id,
       MAX(marks) AS highest_marks,
       MIN(marks) AS lowest_marks
FROM students
GROUP BY class_id;

-- Q4: Write an SQL query to find the total marks scored by students in each class
SELECT class_id, SUM(marks) AS total_marks
FROM students
GROUP BY class_id;


-- PART D – QUERY BASED (JOINS)
-- Q1: Write an SQL query to display student name in uppercase and class name using JOIN
SELECT UPPER(s.student_name) AS student_name, c.class_name
FROM students s
JOIN classes c ON s.class_id = c.class_id;

-- Q2: Write an SQL query to display class name and total number of students using JOIN
SELECT c.class_name, COUNT(s.student_id) AS total_students
FROM classes c
JOIN students s ON c.class_id = s.class_id
GROUP BY c.class_name;

-- Q3: Write an SQL query to display student name and marks using JOIN
SELECT s.student_name, s.marks
FROM students s
JOIN classes c ON s.class_id = c.class_id;

-- Q4: Write an SQL query to display class name and average marks using JOIN and aggregate function
SELECT c.class_name, AVG(s.marks) AS avg_marks
FROM classes c
JOIN students s ON c.class_id = s.class_id
GROUP BY c.class_name;