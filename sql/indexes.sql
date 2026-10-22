-- Foreign key indexes
CREATE INDEX idx_fact_company ON fact_jobs(company_id);
CREATE INDEX idx_fact_location ON fact_jobs(location_id);
CREATE INDEX idx_fact_salary ON fact_jobs(salary_id);

-- Composite index
CREATE INDEX idx_country_experience
ON dim_location(country, city);
