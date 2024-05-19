import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Line"
    PROJECT_VERSION: str = "1.0.0"
    admin_email: str = "89831023404@mail.ru"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST","localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = (f"postqresql://{POSTGRES_USER}:"
                    f"{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
                    f"{POSTGRES_PORT}/{POSTGRES_DB}")

settings = Settings()

