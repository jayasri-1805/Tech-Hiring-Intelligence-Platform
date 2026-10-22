DELIMITER //

CREATE FUNCTION AverageSalary()
RETURNS DECIMAL(12,2)
DETERMINISTIC
BEGIN
    DECLARE avg_sal DECIMAL(12,2);

    SELECT AVG(salary_midpoint)
    INTO avg_sal
    FROM dim_salary;

    RETURN avg_sal;
END //

DELIMITER ;

SELECT AverageSalary();
