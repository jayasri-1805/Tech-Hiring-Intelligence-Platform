-- Maintenance Examples

ANALYZE TABLE fact_jobs;
ANALYZE TABLE dim_company;

OPTIMIZE TABLE fact_jobs;

-- Backup reminder:
-- mysqldump -u <user> -p thip > thip_backup.sql
