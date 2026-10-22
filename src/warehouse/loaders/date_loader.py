import pandas as pd

class DateLoader:
    def prepare(self, dataframe: pd.DataFrame):
        date = dataframe[[
            "posted_year",
            "job_market_phase",
            "years_since_posted"
        ]].drop_duplicates()
        return date.reset_index(drop=True)
