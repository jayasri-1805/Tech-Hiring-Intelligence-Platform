CREATE TABLE dim_company(
 company_id INT PRIMARY KEY AUTO_INCREMENT,
 company_name VARCHAR(255),
 company_size VARCHAR(50),
 company_category VARCHAR(50),
 industry VARCHAR(100)
);

CREATE TABLE dim_location(
 location_id INT PRIMARY KEY AUTO_INCREMENT,
 country VARCHAR(100),
 city VARCHAR(100)
);

CREATE TABLE dim_date(
 date_id INT PRIMARY KEY AUTO_INCREMENT,
 posted_year INT,
 job_market_phase VARCHAR(50),
 years_since_posted INT
);

CREATE TABLE dim_experience(
 experience_id INT PRIMARY KEY AUTO_INCREMENT,
 experience_level VARCHAR(50),
 experience_bucket VARCHAR(50),
 min_experience_years INT
);

CREATE TABLE dim_remote(
 remote_id INT PRIMARY KEY AUTO_INCREMENT,
 remote_type VARCHAR(50),
 remote_category VARCHAR(50),
 is_remote BOOLEAN
);

CREATE TABLE dim_salary(
 salary_id INT PRIMARY KEY AUTO_INCREMENT,
 salary_min_usd INT,
 salary_max_usd INT,
 salary_midpoint DECIMAL(12,2),
 salary_band VARCHAR(30)
);

CREATE TABLE fact_jobs(
 job_id INT PRIMARY KEY,
 company_id INT,
 location_id INT,
 date_id INT,
 experience_id INT,
 remote_id INT,
 salary_id INT,
 salary_range DECIMAL(12,2),
 high_paying_job BOOLEAN,
 FOREIGN KEY(company_id) REFERENCES dim_company(company_id),
 FOREIGN KEY(location_id) REFERENCES dim_location(location_id),
 FOREIGN KEY(date_id) REFERENCES dim_date(date_id),
 FOREIGN KEY(experience_id) REFERENCES dim_experience(experience_id),
 FOREIGN KEY(remote_id) REFERENCES dim_remote(remote_id),
 FOREIGN KEY(salary_id) REFERENCES dim_salary(salary_id)
);
