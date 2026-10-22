-- Case Study 1: Top hiring countries
SELECT dl.country, COUNT(*) AS total_jobs
FROM fact_jobs f
JOIN dim_location dl USING(location_id)
GROUP BY dl.country
ORDER BY total_jobs DESC;

-- Case Study 2: Average salary by experience
SELECT de.experience_level,
       ROUND(AVG(ds.salary_midpoint),2) AS avg_salary
FROM fact_jobs f
JOIN dim_experience de USING(experience_id)
JOIN dim_salary ds USING(salary_id)
GROUP BY de.experience_level
ORDER BY avg_salary DESC;

-- Case Study 3: Remote jobs by company category
SELECT dc.company_category,
       SUM(CASE WHEN dr.is_remote=1 THEN 1 ELSE 0 END) AS remote_jobs
FROM fact_jobs f
JOIN dim_company dc USING(company_id)
JOIN dim_remote dr USING(remote_id)
GROUP BY dc.company_category;
