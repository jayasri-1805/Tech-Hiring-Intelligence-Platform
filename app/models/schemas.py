from pydantic import BaseModel


class PredictionRequest(BaseModel):
    job_title: str
    company_type: str
    industry: str
    country: str
    city: str
    remote_type: str
    experience_level: str
    min_experience_years: int
    employment_type: str
    posted_year: int
    company_size: str
    experience_bucket: str
    remote_category: str
    is_remote: int
    company_size_rank: int
    company_category: str
    job_market_phase: str
    years_since_posted: int
    dataset_version: str


class PredictionResponse(BaseModel):
    predicted_salary: float