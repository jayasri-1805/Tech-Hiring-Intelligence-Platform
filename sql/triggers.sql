DELIMITER //

CREATE TRIGGER trg_fact_jobs_insert
AFTER INSERT ON fact_jobs
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, record_id)
    VALUES ('fact_jobs', 'INSERT', NEW.job_id);
END //

CREATE TRIGGER trg_fact_jobs_update
AFTER UPDATE ON fact_jobs
FOR EACH ROW
BEGIN
    INSERT INTO audit_log(table_name, operation_type, record_id)
    VALUES ('fact_jobs', 'UPDATE', NEW.job_id);
END //

DELIMITER ;
