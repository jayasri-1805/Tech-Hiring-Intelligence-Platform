import pandas as pd

class HiringKPIs:
    def calculate(self, df: pd.DataFrame)->dict:
        return {
            "total_jobs": int(len(df)),
            "remote_jobs": int(df["is_remote"].sum()),
            "remote_percentage": round(df["is_remote"].mean()*100,2)
        }
