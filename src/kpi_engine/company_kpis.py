import pandas as pd

class CompanyKPIs:
    def calculate(self, df: pd.DataFrame)->dict:
        return {
            "small_companies": int((df["company_size_rank"]==1).sum()),
            "medium_companies": int((df["company_size_rank"]==2).sum()),
            "large_companies": int((df["company_size_rank"]==3).sum())
        }
