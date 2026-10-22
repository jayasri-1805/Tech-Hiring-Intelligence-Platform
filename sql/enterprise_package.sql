-- Enterprise SQL Package

SOURCE indexes.sql;
SOURCE stored_procedures.sql;
SOURCE stored_functions.sql;
SOURCE triggers.sql;

-- Verification
SHOW TABLES;
SHOW INDEX FROM fact_jobs;
SELECT COUNT(*) FROM fact_jobs;
