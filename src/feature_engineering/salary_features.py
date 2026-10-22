import pandas as pd

class SalaryFeatures:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result=df.copy()
        result["salary_midpoint"]=(result["salary_min_usd"]+result["salary_max_usd"])/2
        result["salary_range"]=result["salary_max_usd"]-result["salary_min_usd"]
        result["high_paying_job"]=result["salary_midpoint"]>=150000
        result["salary_band"]=pd.cut(
            result["salary_midpoint"],
            bins=[0,50000,100000,150000,250000,float("inf")],
            labels=["Low","Medium","High","Very High","Premium"],
            include_lowest=True
        )
        return result
