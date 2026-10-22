from pathlib import Path
import json
import pandas as pd

class AnalyticsValidator:
    def validate(self, df: pd.DataFrame)->dict:
        result={
            "rows": int(len(df)),
            "columns": int(len(df.columns)),
            "missing_values": int(df.isna().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "status": "PASS"
        }
        if result["missing_values"]>0 or result["duplicate_rows"]>0:
            result["status"]="WARNING"
        Path("reports").mkdir(exist_ok=True)
        with open("reports/analytics_validation.json","w",encoding="utf-8") as f:
            json.dump(result,f,indent=4)
        print("Analytics validation completed.")
        return result
