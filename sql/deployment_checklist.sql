-- Deployment Verification

SHOW TABLES;

SELECT COUNT(*) FROM fact_jobs;

SELECT COUNT(*) FROM dim_company;
SELECT COUNT(*) FROM dim_location;
SELECT COUNT(*) FROM dim_salary;

SHOW INDEX FROM fact_jobs;
