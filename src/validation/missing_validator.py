import pandas as pd

class MissingValueValidator:
    def validate(self,df:pd.DataFrame)->pd.DataFrame:
        report=df.isna().sum().to_frame("missing_count")
        report["missing_percent"]=(report["missing_count"]/len(df)*100).round(2)
        return report
