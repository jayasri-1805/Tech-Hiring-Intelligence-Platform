-- Top Paying Jobs
SELECT
job_title,
salary_midpoint,
RANK() OVER(ORDER BY salary_midpoint DESC) AS salary_rank
FROM fact_jobs
JOIN dim_salary USING(salary_id);
