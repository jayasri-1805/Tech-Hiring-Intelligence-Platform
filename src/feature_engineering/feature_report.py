from pathlib import Path
import json
import pandas as pd

class FeatureReport:
    def generate(self, df: pd.DataFrame):
        report={
            "rows":len(df),
            "columns":len(df.columns),
            "engineered_features":[
                c for c in df.columns if c not in [
                    "job_id","job_title","company_type","industry","country","city",
                    "remote_type","experience_level","min_experience_years",
                    "salary_min_usd","salary_max_usd","employment_type",
                    "posted_year","company_size"
                ]
            ]
        }
        out=Path("reports")
        out.mkdir(exist_ok=True)
        with open(out/"feature_report.json","w",encoding="utf-8") as f:
            json.dump(report,f,indent=4)
        pd.DataFrame({"column":df.columns,"dtype":df.dtypes.astype(str)}).to_csv(
            out/"feature_dictionary.csv",index=False)
        print("Feature reports generated.")
