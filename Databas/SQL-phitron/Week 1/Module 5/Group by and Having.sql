USE dummydb;

SELECT * from employees;

SELECT DISTINCT job_id, max(salary) 
FROM employees
GROUP BY job_id
HAVING max(salary) > 10000;

SELECT DISTINCT hire_date, max(salary) ,count(hire_date)
FROM employees
GROUP BY hire_date;



