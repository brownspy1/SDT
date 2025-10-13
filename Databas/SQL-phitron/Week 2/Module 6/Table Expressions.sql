USE dummydb;

-- I WELL FIND ALL EMPLOYEE WHO GRETER AVG VALU OF IT AND LES THEN MAX OF MARKATING
WITH AVG_OF_IT AS 
	( SELECT AVG(salary) AS avg_salary
	  FROM employees
	  WHERE department_id = 60 
	) , 
    MAX_OF_MKT AS
    (
	  SELECT MAX(salary) AS mx_salary
	  FROM employees
	  WHERE department_id = 20) 
      
	SELECT * 
    FROM employees
    WHERE salary > (SELECT avg_salary FROM AVG_OF_IT) 
	AND salary < (SELECT mx_salary FROM MAX_OF_MKT);