-- Jobs by Country
SELECT dl.country, COUNT(*) AS jobs
FROM fact_jobs f
JOIN dim_location dl
ON f.location_id = dl.location_id
GROUP BY dl.country;

-- Average Salary by Company Category
SELECT dc.company_category,
AVG(ds.salary_midpoint) AS avg_salary
FROM fact_jobs f
JOIN dim_company dc ON f.company_id=dc.company_id
JOIN dim_salary ds ON f.salary_id=ds.salary_id
GROUP BY dc.company_category;
