USE dummydb;

SELECT * FROM EMPLOYEES;

SELECT * 
FROM employees
WHERE salary < (SELECT SALARY FROM employees WHERE employee_id = 144);

SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

SELECT SUM(SALARY)
FROM employees
WHERE job_id = (SELECT job_id FROM jobs WHERE JOB_TITLE = 'PROGRAMMER');