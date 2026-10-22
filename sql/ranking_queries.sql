-- Top 10 highest paying jobs
SELECT
job_title,
salary_midpoint
FROM fact_jobs
JOIN dim_salary USING(salary_id)
ORDER BY salary_midpoint DESC
LIMIT 10;

-- Highest paying company category
SELECT
company_category,
AVG(salary_midpoint) avg_salary
FROM fact_jobs
JOIN dim_company USING(company_id)
JOIN dim_salary USING(salary_id)
GROUP BY company_category
ORDER BY avg_salary DESC;
