import pandas as pd

class RemoteLoader:
    def prepare(self, dataframe: pd.DataFrame):
        remote = dataframe[[
            "remote_type",
            "remote_category",
            "is_remote"
        ]].drop_duplicates()
        return remote.reset_index(drop=True)
