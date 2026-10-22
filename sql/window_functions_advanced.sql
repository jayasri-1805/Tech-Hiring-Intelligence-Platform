-- ROW_NUMBER
SELECT
    job_title,
    salary_midpoint,
    ROW_NUMBER() OVER(ORDER BY salary_midpoint DESC) AS row_num
FROM fact_jobs
JOIN dim_salary USING(salary_id);

-- DENSE_RANK
SELECT
    job_title,
    salary_midpoint,
    DENSE_RANK() OVER(ORDER BY salary_midpoint DESC) AS dense_rank
FROM fact_jobs
JOIN dim_salary USING(salary_id);

-- LAG
SELECT
    posted_year,
    COUNT(*) AS jobs,
    LAG(COUNT(*)) OVER(ORDER BY posted_year) AS previous_year_jobs
FROM fact_jobs
JOIN dim_date USING(date_id)
GROUP BY posted_year;
