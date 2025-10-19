-- select all the job catagory with dont have any employee

SELECT departments.department_name
	FROM departments
		LEFT JOIN employees ON departments.department_id = employees.department_id 
			WHERE employees.department_id IS NULL;
        
        
        
-- find all employys jara tader department er avg salaryr teke koto taka kom pay

SELECT 
employees.first_name,
employees.salary, 
(SELECT AVG(salary) FROM employees WHERE department_id = employees.department_id) - employees.salary as diff_salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id;



-- kon kon department er minimum salary gretar 5000
SELECT department_name, MIN(salary)
FROM employees E
JOIN departments D ON E.department_id = D.department_id
GROUP BY department_name
HAVING MIN(salary) > 5000;




