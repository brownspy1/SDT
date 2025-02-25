--use for bpi databas
SELECT * 
FROM student_details;

SELECT roll, name 
FROM student_details;

SELECT DISTINCT city, name 
FROM student_details;

SELECT * 
FROM student_details 
WHERE city = 'Barisal';

SELECT * 
FROM student_details
 WHERE marks > 80;

SELECT * 
FROM student_details 
WHERE marks BETWEEN 70 AND 90;

SELECT * 
FROM student_details 
WHERE city = 'Barisal' OR marks > 80;

SELECT *
FROM student_details
WHERE marks BETWEEN 60 AND 70;

SELECT * 
FROM student_details 
WHERE city IN ("Barisal","Dhaka","Rangpur");

SELECT * 
FROM student_details 
WHERE city NOT IN ("Dhaka","Rangpur") LIMIT 2; 

SELECT *
FROM student_list
-- WHERE marks BETWEEN 80 AND 90
ORDER BY Your Name: DESC;