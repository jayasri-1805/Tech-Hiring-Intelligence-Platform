DELIMITER //

CREATE PROCEDURE GetJobsByCountry(IN p_country VARCHAR(100))
BEGIN
    SELECT f.job_title,
           dl.country,
           ds.salary_midpoint
    FROM fact_jobs f
    JOIN dim_location dl USING(location_id)
    JOIN dim_salary ds USING(salary_id)
    WHERE dl.country = p_country;
END //

DELIMITER ;

CALL GetJobsByCountry('United States');
