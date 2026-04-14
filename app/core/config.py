from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # JWT
    secret_ky: str
    algorithm: str
    access_token_minutes: int
    refresh_token_days: int

    # DATABASE
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()
