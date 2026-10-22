import pandas as pd

class RemoteFeatures:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()

        result["remote_category"] = (
            result["remote_type"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        result["is_remote"] = (
            result["remote_category"]
            .eq("Remote")
            .astype(int)
        )

        return result
