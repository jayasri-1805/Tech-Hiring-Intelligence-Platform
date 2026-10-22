-- Jobs above overall average salary
SELECT job_title
FROM fact_jobs f
JOIN dim_salary ds ON f.salary_id=ds.salary_id
WHERE ds.salary_midpoint >
(
SELECT AVG(salary_midpoint)
FROM dim_salary
);
