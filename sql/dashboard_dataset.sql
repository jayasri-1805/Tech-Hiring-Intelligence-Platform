-- Master dataset for Power BI
SELECT
    f.job_id,
    f.job_title,
    dc.company_category,
    dl.country,
    de.experience_level,
    dr.remote_category,
    ds.salary_midpoint,
    dd.posted_year
FROM fact_jobs f
JOIN dim_company dc USING(company_id)
JOIN dim_location dl USING(location_id)
JOIN dim_experience de USING(experience_id)
JOIN dim_remote dr USING(remote_id)
JOIN dim_salary ds USING(salary_id)
JOIN dim_date dd USING(date_id);
