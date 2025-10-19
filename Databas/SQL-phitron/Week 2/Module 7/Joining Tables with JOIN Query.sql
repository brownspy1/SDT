SELECT employees.first_name , departments.department_name 
FROM employees
    JOIN departments 
        ON departments.department_id = employees.department_id;


SELECT  employees.first_name,employees.last_name,departments.department_name 
FROM employees
    JOIN departments USING (department_id);