-- Execution Plan Examples

EXPLAIN FORMAT=TRADITIONAL
SELECT f.job_title,
       ds.salary_midpoint
FROM fact_jobs f
JOIN dim_salary ds USING(salary_id)
WHERE ds.salary_midpoint > 120000;

EXPLAIN ANALYZE
SELECT dl.country,
       COUNT(*) AS total_jobs
FROM fact_jobs f
JOIN dim_location dl USING(location_id)
GROUP BY dl.country;
