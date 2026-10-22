from datetime import datetime
import pandas as pd

class MetadataGenerator:
    def generate(self, df: pd.DataFrame)->dict:
        return {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "rows": int(len(df)),
            "columns": int(len(df.columns)),
            "version": "THIP_v0.2"
        }
