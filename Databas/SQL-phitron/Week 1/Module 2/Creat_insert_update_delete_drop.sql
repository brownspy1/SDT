CREATE DATABASE IF NOT EXISTS phitron_sdt;
USE phitron_sdt;

CREATE TABLE student(
	roll CHAR(4) PRIMARY KEY,
    name VARCHAR(50),
    marks DOUBLE
);

-- delete full tabile
DROP TABLE student;

-- student 1
INSERT INTO student 
(roll,name,marks) VALUES
(0001,"M.Mahir",80);

-- student 2
INSERT INTO student
(roll,name,marks)VALUES
(0002,"M.Mahadi",70);

-- Update student 2
SET SQL_SAFE_UPDATES = 0;
UPDATE student SET name = "Abdulla al mahir" WHERE roll = 1;
SET SQL_SAFE_UPDATES = 1;

-- DELETE user 2
SET SQL_SAFE_UPDATES = 0;
DELETE FROM student WHERE roll = 2;
SET SQL_SAFE_UPDATES = 1;

-- show all data from student tabile
SELECT * FROM student;


