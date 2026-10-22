import pandas as pd

class NumericProfiler:
    def generate(self,df: pd.DataFrame):
        return df.describe()
