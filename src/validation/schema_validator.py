import pandas as pd

REQUIRED_COLUMNS=[
    "job_id","job_title","company_type","industry","country","city",
    "remote_type","experience_level","min_experience_years",
    "salary_min_usd","salary_max_usd","employment_type",
    "posted_year","company_size"
]

class SchemaValidator:
    def validate(self,df:pd.DataFrame)->None:
        missing=[c for c in REQUIRED_COLUMNS if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        print("✓ Schema validation passed")
