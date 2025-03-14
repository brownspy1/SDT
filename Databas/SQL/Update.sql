use bpi;
SELECT * FROM student_details;

SET SQL_SAFE_UPDATES = 0; -- if 0 safe mode off if 1 safe mode on

ALTER TABLE bpi_student
MODIFY grade VARCHAR(2);

UPDATE bpi_student
SET grade = 'A+'
WHERE grade = 'A';

DELETE FROM student_details
WHERE roll = 743679;


-- add,delete update edit colume
-- add column
ALTER TABLE bpi_student
ADD COLUMN age INT NOT NULL DEFAULT 18;

-- delete column
ALTER TABLE bpi_student
DROP  COLUMN ranking;

-- update column
ALTER TABLE bpi_student
MODIFY age VARCHAR(20);

-- rename Table
ALTER TABLE student_details
RENAME TO bpi_student;

-- rename column
ALTER TABLE bpi_student
CHANGE COLUMN age ranking INT;

--remove table data not table

TRUNCATE TABLE bpi_student;

SELECT * FROM bpi_student;