import pandas as pd

class DatasetSummary:
    def generate(self,df: pd.DataFrame)->dict:
        return {"rows":len(df),"columns":len(df.columns),"memory_mb":round(df.memory_usage(deep=True).sum()/(1024**2),2)}
