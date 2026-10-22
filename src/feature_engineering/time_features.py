import pandas as pd

class TimeFeatures:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result=df.copy()

        def phase(year):
            if year<=2021:
                return "Pre-AI Boom"
            elif year<=2023:
                return "AI Boom"
            else:
                return "Modern AI"

        result["job_market_phase"]=result["posted_year"].apply(phase)
        result["years_since_posted"]=2026-result["posted_year"]
        result["dataset_version"]="THIP_v0.2"

        return result
