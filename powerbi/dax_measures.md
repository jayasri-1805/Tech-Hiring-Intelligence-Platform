# Core DAX Measures

Total Jobs = COUNTROWS(fact_jobs)

Average Salary =
AVERAGE(dim_salary[salary_midpoint])

High Paying Jobs =
CALCULATE(
    COUNTROWS(fact_jobs),
    fact_jobs[high_paying_job] = TRUE()
)

Remote Job % =
DIVIDE(
    CALCULATE(COUNTROWS(fact_jobs), dim_remote[is_remote]=TRUE()),
    COUNTROWS(fact_jobs)
)
