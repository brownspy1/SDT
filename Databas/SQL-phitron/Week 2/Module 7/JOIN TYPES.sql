-- JOIN HASE 4 TYPE
-- 1 INNER JOIN
-- 2 LEFT JOIN
-- 3 RIGHT JOIN
-- 4 CROSS JOIN

-- SELECT employees.first_name, departments.department_name 
-- FROM employees
--     CROSS JOIN departments USING(department_id);

SELECT employees.first_name, departments.department_name 
FROM employees
    RIGHT JOIN departments USING(department_id);