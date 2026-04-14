from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_password: str
    redis_password: str

settings = Settings()
