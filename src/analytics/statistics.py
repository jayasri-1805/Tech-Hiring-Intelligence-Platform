import pandas as pd

class StatisticalAnalysis:

    def descriptive_statistics(self, df: pd.DataFrame):
        return df.describe(include="all")

    def outlier_summary(self, df: pd.DataFrame):
        result = {}
        for col in df.select_dtypes(include="number").columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            result[col] = int(((df[col] < lower) | (df[col] > upper)).sum())
        return result
