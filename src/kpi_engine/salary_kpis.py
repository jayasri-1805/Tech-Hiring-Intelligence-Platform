import pandas as pd

class SalaryKPIs:
    def calculate(self, df: pd.DataFrame)->dict:
        return {
            "average_salary": round(df["salary_midpoint"].mean(),2),
            "median_salary": round(df["salary_midpoint"].median(),2),
            "maximum_salary": round(df["salary_max_usd"].max(),2),
            "minimum_salary": round(df["salary_min_usd"].min(),2)
        }
