-- Remote job ratio
SELECT
ROUND(
100*SUM(CASE WHEN dr.is_remote=1 THEN 1 ELSE 0 END)/COUNT(*),
2
) AS remote_percentage
FROM fact_jobs f
JOIN dim_remote dr
ON f.remote_id=dr.remote_id;
