SELECT*
FROM parks_and_recreation.employee_demographics;

-- GROUP BY
SELECT gender,avg(age)
FROM employee_demographics
GROUP BY gender;

-- ORDER BY
SELECT *
FROM employee_demographics
ORDER BY birth_date desc;
