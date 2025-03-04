use bpi;

SELECT city, count(name) AS st_count, group_concat(name separator ', ') AS Student
FROM student_details
GROUP BY city;

SELECT city, count(name)
FROM student_details
GROUP BY city;

-- condition in group using keyword or close Having

use bpi;

SELECT * FROM student_details;

SELECT city ,count(name)
FROM student_details
WHERE grade = 'A'
GROUP BY city
HAVING MAX(marks) > 90;


