import pandas as pd

class SalaryLoader:
    def prepare(self, dataframe: pd.DataFrame):
        salary = dataframe[[
            "salary_min_usd",
            "salary_max_usd",
            "salary_midpoint",
            "salary_band"
        ]].drop_duplicates()
        return salary.reset_index(drop=True)
