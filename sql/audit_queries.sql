-- View audit history
SELECT *
FROM audit_log
ORDER BY changed_at DESC;

-- Count operations
SELECT operation_type,
COUNT(*) AS total_operations
FROM audit_log
GROUP BY operation_type;
