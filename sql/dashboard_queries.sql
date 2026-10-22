-- Dashboard KPI: Total Jobs
SELECT COUNT(*) total_jobs FROM fact_jobs;

-- Dashboard KPI: Average Salary
SELECT AVG(salary_midpoint) avg_salary
FROM dim_salary;

-- Dashboard KPI: Remote Percentage
SELECT
ROUND(
100*SUM(CASE WHEN is_remote=1 THEN 1 ELSE 0 END)/COUNT(*),2
) remote_percentage
FROM fact_jobs
JOIN dim_remote USING(remote_id);
