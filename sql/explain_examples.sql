EXPLAIN
SELECT f.job_title, ds.salary_midpoint
FROM fact_jobs f
JOIN dim_salary ds USING(salary_id)
WHERE ds.salary_midpoint > 100000;

EXPLAIN
SELECT country, COUNT(*)
FROM fact_jobs
JOIN dim_location USING(location_id)
GROUP BY country;
