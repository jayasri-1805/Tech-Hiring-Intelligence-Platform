import pandas as pd

class ExperienceLoader:
    def prepare(self, dataframe: pd.DataFrame):
        exp = dataframe[[
            "experience_level",
            "experience_bucket",
            "min_experience_years"
        ]].drop_duplicates()
        return exp.reset_index(drop=True)
