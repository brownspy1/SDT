CREATE DATABASE IF NOT EXISTS xyz;
USE xyz;
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
);

INSERT INTO employee (id, name, salary)
VALUES 
    (1, 'adam', 25000),
    (2, 'bob', 36555),
    (3, 'jack', 78522);

SELECT * FROM employee;
DROP DATABASE XYZ;