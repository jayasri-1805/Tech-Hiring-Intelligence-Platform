from pathlib import Path
from .duplicate_handler import DuplicateHandler
from .missing_handler import MissingValueHandler
from .salary_cleaner import SalaryCleaner
from .exporter import DataExporter

class DataCleaner:
    def run(self, df):
        original=len(df)
        df=DuplicateHandler().clean(df)
        df=MissingValueHandler().clean(df)
        df=SalaryCleaner().clean(df)
        DataExporter().export(df)

        report=Path("reports")
        report.mkdir(exist_ok=True)
        with open(report/"cleaning_report.txt","w",encoding="utf-8") as f:
            f.write(f"Original Rows : {original}\n")
            f.write(f"Final Rows    : {len(df)}\n")
            f.write(f"Rows Removed  : {original-len(df)}\n")
        print("Cleaning completed.")
        print("Processed dataset saved to data/processed/clean_ai_jobs.csv")
        return df
