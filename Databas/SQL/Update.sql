use bpi;
SELECT * FROM student_details;

SET SQL_SAFE_UPDATES = 0; -- if 0 safe mode off if 1 safe mode on

ALTER TABLE student_details
MODIFY grade VARCHAR(2);

UPDATE student_details
SET grade = 'A+'
WHERE grade = 'O';

DELETE FROM student_details
WHERE roll = 743679;