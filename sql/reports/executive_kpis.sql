SELECT COUNT(*) AS total_jobs FROM fact_jobs;

SELECT ROUND(AVG(salary_midpoint),2) AS average_salary
FROM dim_salary;

SELECT company_category,
COUNT(*) AS jobs
FROM vw_job_summary
GROUP BY company_category
ORDER BY jobs DESC;

SELECT country,
COUNT(*) AS jobs
FROM vw_job_summary
GROUP BY country
ORDER BY jobs DESC;
