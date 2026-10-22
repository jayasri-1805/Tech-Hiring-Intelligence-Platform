-- CTE: Average salary by country
WITH country_salary AS (
SELECT dl.country, AVG(ds.salary_midpoint) avg_salary
FROM fact_jobs f
JOIN dim_location dl ON f.location_id=dl.location_id
JOIN dim_salary ds ON f.salary_id=ds.salary_id
GROUP BY dl.country
)
SELECT * FROM country_salary
ORDER BY avg_salary DESC;
