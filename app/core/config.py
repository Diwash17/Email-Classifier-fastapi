from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str
    VECTORIZER_PATH: str
    ENV: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()