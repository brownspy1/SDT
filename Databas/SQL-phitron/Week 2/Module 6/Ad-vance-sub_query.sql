use dummydb;

SELECT * 
FROM employees
WHERE SALARY = (SELECT MAX(salary)
		FROM employees
		WHERE salary < (
						SELECT MAX(SALARY)
						FROM employees
						)
					);
			
            
SELECT * 
FROM employees as EM
WHERE salary > (SELECT salary 
				FROM employees AS MGR 
                WHERE EM.manager_id = MGR.employee_id); 
                

SELECT * 
FROM employees AS EM
WHERE job_id = (SELECT job_id 
				FROM employees AS MG
                WHERE EM.manager_id = MG.employee_id);