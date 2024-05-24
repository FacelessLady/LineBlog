import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Line"
    PROJECT_VERSION: str = "1.0.0"
    ADMIN_EMAIL: str = "89831023404@mail.ru"
    POSTGRES_DATABASE_URL: str

    def __init__(self):
        self.POSTGRES_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:" \
                                     f"{os.environ['POSTGRES_PASSWORD']}@" \
                                     f"{os.environ['POSTGRES_HOST']}:" \
                                     f"{os.environ['POSTGRES_PORT']}/" \
                                     f"{os.environ['POSTGRES_DB']}"

settings = Settings()

