from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    experience_level:str=Field(min_length=1)
    company_category:str=Field(min_length=1)
    country:str=Field(min_length=1)
    remote_category:str=Field(min_length=1)
