from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEWS_API_KEY: str
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
