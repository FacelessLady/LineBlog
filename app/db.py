from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy.orm import sessionmaker
from typing import Any

from app.config import settings

# Определяем параметры для подключения
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("URL-адрес базы данных:", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base:
    id: Any
    __name__: str

    # Генерируем имя таблицы из имени класса
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()