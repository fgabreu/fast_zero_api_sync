from pydantic_settings import BaseSettings, SettingsConigDict


class Settings(BaseSettings):
    model_config = SettingsConigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    
    DATABASE_URL: str

    