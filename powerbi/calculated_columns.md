# Example Calculated Columns

Salary Category =
IF(
    dim_salary[salary_midpoint] >= 100000,
    "High",
    "Standard"
)

Remote Label =
IF(
    dim_remote[is_remote],
    "Remote",
    "Non-Remote"
)
