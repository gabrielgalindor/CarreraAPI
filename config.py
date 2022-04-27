import json
from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Interface API"
    DEVICE_USER: str
    DEVICE_PASS: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

@lru_cache(maxsize=128)
def get_settings() -> Settings:
    set_vars = Settings()
    return set_vars

settings = get_settings()