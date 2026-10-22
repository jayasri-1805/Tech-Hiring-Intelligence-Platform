from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_title: str = "THIP API"
    api_version: str = "1.0.0"
    api_key: str = "change_me"

settings = Settings()
