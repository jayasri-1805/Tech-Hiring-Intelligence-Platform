-- Hiring trend by year
SELECT dd.posted_year,
COUNT(*) total_jobs
FROM fact_jobs f
JOIN dim_date dd ON f.date_id=dd.date_id
GROUP BY dd.posted_year
ORDER BY dd.posted_year;
