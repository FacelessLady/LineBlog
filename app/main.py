from fastapi import FastAPI, Depends, HTTPException
from app.config import settings 
from sqlalchemy.orm import Session
from app.db import engine, SessionLocal, Base
from typing import Generator, List
from app import crud, schemas
from fastapi.responses import FileResponse
from datetime import datetime
import uvicorn

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app    

app = start_application()

def get_db() -> Generator: 
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Электронная почта уже зарегистрирована")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user

@app.post("/users/{user_id}/blogs/", response_model=schemas.Blog)
def create_blog_for_user(user_id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db=db, blog=blog, user_id=user_id)

@app.get("/blogs/", response_model=List[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@app.on_event("startup")
def on_startup():
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: Begin\n')

@app.on_event("shutdown")
def shutdown():
    with open("log_p.txt", mode="a") as log:
        log.write(f'{datetime.utcnow()}: End\n')

@app.get("/")
def main():
    return FileResponse("files/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6000)
