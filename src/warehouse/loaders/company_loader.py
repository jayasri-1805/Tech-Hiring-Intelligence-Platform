import pandas as pd

class CompanyLoader:
    def prepare(self, dataframe: pd.DataFrame):
        company = dataframe[[
            "company_type",
            "company_size",
            "company_category",
            "industry"
        ]].drop_duplicates()
        return company.reset_index(drop=True)
