import pandas as pd

class CategoricalProfiler:
    def generate(self,df: pd.DataFrame):
        return df.describe(include="object")
