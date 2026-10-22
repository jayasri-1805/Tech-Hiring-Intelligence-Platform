import pandas as pd

REQUIRED_FEATURES = [
    "salary_midpoint","salary_range","salary_band","high_paying_job",
    "experience_bucket","remote_category","is_remote",
    "company_size_rank","company_category",
    "job_market_phase","years_since_posted","dataset_version"
]

class FeatureValidator:
    def validate(self, df: pd.DataFrame):
        missing=[c for c in REQUIRED_FEATURES if c not in df.columns]
        if missing:
            raise ValueError(f"Missing engineered features: {missing}")
        print("Feature validation passed.")
