from sqlalchemy import create_engine,  text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, sessionmaker
from typing import Any

from core.config import settings

# Определяем параметры для подключения
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("URL-адрес базы данных",SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
db_session = SessionLocal


@as_declarative()
class Base:
    id: Any
    __name__: str

    #генерируем имя таблицы из имени класса
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()