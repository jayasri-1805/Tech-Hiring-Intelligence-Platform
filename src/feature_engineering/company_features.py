import pandas as pd

class CompanyFeatures:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()

        rank = {
            "Small": 1,
            "Medium": 2,
            "Large": 3
        }

        result["company_size_rank"] = (
            result["company_size"]
            .map(rank)
            .fillna(0)
            .astype(int)
        )

        growth = {
            "Small": "Startup",
            "Medium": "Scale-up",
            "Large": "Enterprise"
        }

        result["company_category"] = (
            result["company_size"]
            .map(growth)
            .fillna("Unknown")
        )

        return result
