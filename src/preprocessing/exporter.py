from pathlib import Path
import pandas as pd

class DataExporter:
    def export(self, df: pd.DataFrame) -> None:
        output_dir = Path("data/processed")
        output_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_dir/"clean_ai_jobs.csv", index=False)
