from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, select
from app.config import settings
from app.models import Base, Blog, User

# Определяем параметры для подключения
SQLALCHEMY_DATABASE_URL = settings.POSTGRES_DATABASE_URL
print("URL-адрес базы данных:", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def f():
    with SessionLocal() as session:
        answer = session.execute(text('SELECT * FROM users;'))
        print(f"answer = {answer.all()}")

def f_bilder():
    with SessionLocal() as session:
        query = insert(Blog).values(title="Line")
        session.execute(query)
        session.commit()
        query = select(User)
        answer = session.execute(query)
        print(f"answer = {answer.all()}")