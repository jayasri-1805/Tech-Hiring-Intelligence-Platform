# Power BI Data Model

Fact Table:
- fact_jobs

Dimensions:
- dim_company
- dim_location
- dim_date
- dim_experience
- dim_remote
- dim_salary

Relationships:
Each dimension has a 1:* relationship with fact_jobs using its surrogate key.
