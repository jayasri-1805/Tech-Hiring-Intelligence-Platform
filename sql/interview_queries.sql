-- Q1 Highest paying country
SELECT dl.country,
AVG(ds.salary_midpoint) avg_salary
FROM fact_jobs f
JOIN dim_location dl USING(location_id)
JOIN dim_salary ds USING(salary_id)
GROUP BY dl.country
ORDER BY avg_salary DESC
LIMIT 1;

-- Q2 Top 5 company categories by jobs
SELECT dc.company_category,
COUNT(*) jobs
FROM fact_jobs f
JOIN dim_company dc USING(company_id)
GROUP BY dc.company_category
ORDER BY jobs DESC
LIMIT 5;
