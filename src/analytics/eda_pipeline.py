import pandas as pd

class EDAPipeline:
    def run(self, df: pd.DataFrame):
        return {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": df.isna().sum().to_dict(),
            "numeric_summary": df.describe(include="number")
        }
