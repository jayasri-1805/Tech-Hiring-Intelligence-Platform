CREATE OR REPLACE VIEW vw_job_summary AS
SELECT
    f.job_id,
    f.job_title,
    dc.company_category,
    dl.country,
    de.experience_level,
    ds.salary_midpoint,
    dr.remote_category
FROM fact_jobs f
JOIN dim_company dc USING(company_id)
JOIN dim_location dl USING(location_id)
JOIN dim_experience de USING(experience_id)
JOIN dim_salary ds USING(salary_id)
JOIN dim_remote dr USING(remote_id);

CREATE OR REPLACE VIEW vw_salary_insights AS
SELECT
    company_category,
    AVG(salary_midpoint) AS avg_salary,
    COUNT(*) AS total_jobs
FROM vw_job_summary
GROUP BY company_category;
