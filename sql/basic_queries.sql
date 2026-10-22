-- 01 Total Jobs
SELECT COUNT(*) AS total_jobs FROM fact_jobs;

-- 02 High Paying Jobs
SELECT COUNT(*) AS high_paying_jobs
FROM fact_jobs
WHERE high_paying_job = TRUE;

-- 03 Jobs by Employment Type
SELECT employment_type, COUNT(*) AS jobs
FROM fact_jobs
GROUP BY employment_type;

-- 04 Top Salary Bands
SELECT ds.salary_band, COUNT(*) AS jobs
FROM fact_jobs f
JOIN dim_salary ds ON f.salary_id = ds.salary_id
GROUP BY ds.salary_band
ORDER BY jobs DESC;

-- 05 Experience Distribution
SELECT de.experience_level, COUNT(*) AS jobs
FROM fact_jobs f
JOIN dim_experience de
ON f.experience_id = de.experience_id
GROUP BY de.experience_level;
