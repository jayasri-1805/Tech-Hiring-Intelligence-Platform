import pandas as pd

class LocationLoader:
    def prepare(self, dataframe: pd.DataFrame):
        location = dataframe[[
            "country",
            "city"
        ]].drop_duplicates()
        return location.reset_index(drop=True)
