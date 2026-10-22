from pathlib import Path
import json
from .dataset_summary import DatasetSummary
from .numeric_profile import NumericProfiler
from .categorical_profile import CategoricalProfiler

class DataProfiler:
    def run(self,df):
        reports=Path("reports")
        reports.mkdir(exist_ok=True)
        summary=DatasetSummary().generate(df)
        print("="*70)
        print("DATA PROFILE")
        print(summary)
        NumericProfiler().generate(df).to_csv(reports/"numeric_profile.csv")
        CategoricalProfiler().generate(df).to_csv(reports/"categorical_profile.csv")
        with open(reports/"dataset_summary.json","w",encoding="utf-8") as f:
            json.dump(summary,f,indent=4)
        print("Reports generated successfully.")
