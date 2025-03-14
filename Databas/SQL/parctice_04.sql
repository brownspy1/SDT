use bpi;

ALTER TABLE bpi_student
CHANGE COLUMN name full_name VARCHAR(50) NOT NULL;

DELETE FROM bpi_student
WHERE marks < 80;

ALTER TABLE bpi_student
DROP COLUMN grade;

SELECT * FROM bpi_student;


