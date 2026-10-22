import pandas as pd

class DuplicateHandler:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates()
