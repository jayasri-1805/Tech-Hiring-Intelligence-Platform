import pandas as pd

class SalaryCleaner:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df["salary_min_usd"] <= df["salary_max_usd"]].copy()
