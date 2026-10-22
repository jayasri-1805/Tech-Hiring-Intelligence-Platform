from pathlib import Path
import pandas as pd

class AnalyticsExporter:
    def export(self, df: pd.DataFrame)->None:
        out=Path("data/analytics")
        out.mkdir(parents=True,exist_ok=True)
        df.to_csv(out/"analytics_dataset.csv",index=False)
