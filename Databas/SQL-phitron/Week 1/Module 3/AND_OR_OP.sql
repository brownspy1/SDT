CREATE TABLE Employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Salary INT NOT NULL,
    Joining_Year INT NOT NULL,
    Age INT NOT NULL
);

INSERT INTO Employee (Name, Salary, Joining_Year, Age) VALUES
('A', 50000, 2021, 40),
('B', 20000, 2023, 30),
('C', 10000, 2023, 20),
('D', 15000, 2022, 25);

SELECT * FROM employee WHERE
Salary > 9000 AND Age < 30;

SELECT * FROM employee WHERE
Salary > 10000 OR (Age > 20 AND Salary <30000);


