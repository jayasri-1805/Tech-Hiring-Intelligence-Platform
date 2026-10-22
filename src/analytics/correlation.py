import pandas as pd

class CorrelationAnalysis:

    def numeric_correlation(self, df: pd.DataFrame):
        return df.select_dtypes(include="number").corr()
