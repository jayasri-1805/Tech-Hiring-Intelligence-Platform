-- Production-ready reporting query

SELECT
    dc.company_category,
    dl.country,
    COUNT(*) AS total_jobs,
    ROUND(AVG(ds.salary_midpoint),2) AS avg_salary
FROM fact_jobs f
JOIN dim_company dc USING(company_id)
JOIN dim_location dl USING(location_id)
JOIN dim_salary ds USING(salary_id)
GROUP BY dc.company_category, dl.country
ORDER BY total_jobs DESC;
