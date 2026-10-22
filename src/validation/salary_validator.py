import pandas as pd

class SalaryValidator:
    def validate(self,df:pd.DataFrame)->pd.DataFrame:
        invalid=df[df["salary_min_usd"]>df["salary_max_usd"]]
        return invalid
