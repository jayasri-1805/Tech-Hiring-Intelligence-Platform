import pandas as pd

class MissingValueHandler:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.fillna({
            "city":"Unknown",
            "industry":"Unknown"
        })
