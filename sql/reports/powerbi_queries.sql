-- Dataset for Power BI
SELECT *
FROM vw_job_summary;

-- Salary by Experience
SELECT
experience_level,
AVG(salary_midpoint) avg_salary
FROM vw_job_summary
GROUP BY experience_level;

-- Remote Distribution
SELECT
remote_category,
COUNT(*) jobs
FROM vw_job_summary
GROUP BY remote_category;
