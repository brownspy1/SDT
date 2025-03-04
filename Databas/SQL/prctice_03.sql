use bpi;

SELECT city,AVG(marks) as mrk
FROM student_details
GROUP BY city
ORDER BY mrk ;