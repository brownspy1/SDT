USE phitron_sdt;

SELECT DISTINCT Joining_Year FROM employee; 

SELECT * FROM employee ORDER BY Joining_Year DESC;

SELECT * FROM employee LIMIT 2 OFFSET 1 ;

SELECT * FROM employee LIMIT 1,2;

SELECT * FROM employee WHERE id IN(1,2);

SELECT * FROM employee WHERE ID NOT IN(1,2);

SET SQL_SAFE_UPDATES = 0;
UPDATE employee SET Name = "Moriom" WHERE ID = 3;

SELECT * FROM employee WHERE NAME LIKE "%MAHIR%";

SELECT NAME AS Student_Name FROM employee;