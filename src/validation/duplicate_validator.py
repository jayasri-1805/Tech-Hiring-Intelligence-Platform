import pandas as pd

class DuplicateValidator:
    def validate(self,df:pd.DataFrame)->int:
        return int(df.duplicated().sum())
