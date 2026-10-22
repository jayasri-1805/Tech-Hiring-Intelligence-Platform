-- Avoid SELECT *
SELECT job_title, employment_type
FROM fact_jobs;

-- Aggregate efficiently
SELECT company_id, COUNT(*) AS total_jobs
FROM fact_jobs
GROUP BY company_id;
