USE thip;

-- =====================================================
-- Drop existing tables (safe re-run)
-- =====================================================

DROP TABLE IF EXISTS fact_jobs;
DROP TABLE IF EXISTS dim_salary;
DROP TABLE IF EXISTS dim_remote;
DROP TABLE IF EXISTS dim_experience;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_location;
DROP TABLE IF EXISTS dim_company;

-- =====================================================
-- Company Dimension
-- =====================================================

CREATE TABLE dim_company (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_type VARCHAR(100) NOT NULL,
    company_size VARCHAR(50) NOT NULL,
    company_category VARCHAR(50) NOT NULL,
    industry VARCHAR(150) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uq_company
    (
        company_type,
        company_size,
        industry
    )
);

-- =====================================================
-- Location Dimension
-- =====================================================

CREATE TABLE dim_location (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uq_location
    (
        country,
        city
    )
);

-- =====================================================
-- Date Dimension
-- =====================================================

CREATE TABLE dim_date (
    date_id INT AUTO_INCREMENT PRIMARY KEY,
    posted_year INT NOT NULL,
    job_market_phase VARCHAR(50) NOT NULL,
    years_since_posted INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uq_date
    (
        posted_year,
        job_market_phase
    )
);

-- =====================================================
-- Experience Dimension
-- =====================================================

CREATE TABLE dim_experience (
    experience_id INT AUTO_INCREMENT PRIMARY KEY,
    experience_level VARCHAR(50) NOT NULL,
    experience_bucket VARCHAR(50) NOT NULL,
    min_experience_years INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uq_experience
    (
        experience_level,
        experience_bucket
    )
);

-- =====================================================
-- Remote Dimension
-- =====================================================

CREATE TABLE dim_remote (
    remote_id INT AUTO_INCREMENT PRIMARY KEY,
    remote_type VARCHAR(50) NOT NULL,
    remote_category VARCHAR(50) NOT NULL,
    is_remote BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE KEY uq_remote
    (
        remote_type,
        remote_category
    )
);

-- =====================================================
-- Salary Dimension
-- =====================================================

CREATE TABLE dim_salary (
    salary_id INT AUTO_INCREMENT PRIMARY KEY,
    salary_min_usd INT NOT NULL,
    salary_max_usd INT NOT NULL,
    salary_midpoint DECIMAL(12,2) NOT NULL,
    salary_band VARCHAR(30) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Fact Table
-- =====================================================

CREATE TABLE fact_jobs (

    job_id VARCHAR(30) PRIMARY KEY,

    company_id INT NOT NULL,
    location_id INT NOT NULL,
    date_id INT NOT NULL,
    experience_id INT NOT NULL,
    remote_id INT NOT NULL,
    salary_id INT NOT NULL,

    salary_range DECIMAL(12,2) NOT NULL,
    high_paying_job BOOLEAN NOT NULL,

    employment_type VARCHAR(50),
    job_title VARCHAR(150),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES dim_company(company_id),

    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES dim_location(location_id),

    CONSTRAINT fk_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id),

    CONSTRAINT fk_experience
        FOREIGN KEY (experience_id)
        REFERENCES dim_experience(experience_id),

    CONSTRAINT fk_remote
        FOREIGN KEY (remote_id)
        REFERENCES dim_remote(remote_id),

    CONSTRAINT fk_salary
        FOREIGN KEY (salary_id)
        REFERENCES dim_salary(salary_id)
);

-- =====================================================
-- Indexes
-- =====================================================

CREATE INDEX idx_company
ON fact_jobs(company_id);

CREATE INDEX idx_location
ON fact_jobs(location_id);

CREATE INDEX idx_date
ON fact_jobs(date_id);

CREATE INDEX idx_experience
ON fact_jobs(experience_id);

CREATE INDEX idx_remote
ON fact_jobs(remote_id);

CREATE INDEX idx_salary
ON fact_jobs(salary_id);