create database learning;

use learning;

CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary INT,
    HireDate DATE
);

INSERT INTO Employee (EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');



-- Q1. Write a query to display every employee and all their data.
 select * from Employee;
 
-- Q2. List only the FirstName, LastName, and Salary of every employee. 
select FirstName,LastName,Salary from Employee;

-- Q3. Show all employees who work in the 'IT' department.
select *
from employee
where Department="IT";

-- Q4. Retrieve employees with a salary greater than 6000.
select *
from employee
where Salary>6000;

-- Q5. List all employees ordered by HireDate from newest to oldest.
select *
from employee
order by HireDate desc;

-- Q6. Show a list of all unique departments present in the table.
select distinct department 
from employee;

-- Q7. Find employees whose first name starts with ‘Aʼ
SELECT *
FROM Employee
WHERE FirstName LIKE 'A%';

-- Q8. Show employees whose salaries are between 4000 and 7000.
select *
from employee
where salary between  4000 and 7000;

-- Q9. Find the average salary of all employees.
SELECT AVG(Salary) AS AverageSalary
FROM Employee;

-- Q10. List each department along with the number of employees, but only include departments with more than 3 employees.
SELECT Department, COUNT(*) AS EmployeeCount
FROM Employee
GROUP BY Department
HAVING COUNT(*) > 3;




