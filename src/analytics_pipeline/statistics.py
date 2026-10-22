import pandas as pd

class DatasetStatistics:
    def generate(self, df: pd.DataFrame)->dict:
        return {
            "numeric_columns": len(df.select_dtypes(include="number").columns),
            "categorical_columns": len(df.select_dtypes(exclude="number").columns),
            "missing_values": int(df.isna().sum().sum())
        }
