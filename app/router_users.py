from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Создание нового пользователя
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Чтение пользователя по ID
@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user

# Обновление пользователя по ID
@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return crud.update_user(db=db, user_id=user_id, user=user)

# Исправление пользователя по ID
@router.patch("/{user_id}", response_model=schemas.User)
def patch_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return crud.patch_user(db=db, user_id=user_id, user=user)

# Удаление пользователя по ID
@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return crud.delete_user(db=db, user_id=user_id)

# Получение всех пользователей
@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Создание блога для пользователя
@router.post("/{user_id}/blogs/", response_model=schemas.Blog)
def create_blog_for_user(user_id: int, blog: schemas.BlogCreate, db: Session = Depends(get_session)):
    return crud.create_blog(db=db, blog=blog, user_id=user_id)

# Чтение блогов пользователя
@router.get("/{user_id}/blogs/", response_model=List[schemas.Blog])
def read_blogs_for_user(user_id: int, db: Session = Depends(get_session)):
    blogs = crud.get_blogs_by_user(db, user_id=user_id)
    return blogs

# Обновление блога
@router.put("/{user_id}/blogs/{blog_id}", response_model=schemas.Blog)
def update_blog(user_id: int, blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_session)):
    db_blog = crud.get_blog(db, blog_id=blog_id, user_id=user_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Блог не найден")
    return crud.update_blog(db=db, blog_id=blog_id, blog=blog)

# Исправление блога
@router.patch("/{user_id}/blogs/{blog_id}", response_model=schemas.Blog)
def patch_blog(user_id: int, blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_session)):
    db_blog = crud.get_blog(db, blog_id=blog_id, user_id=user_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Блог не найден")
    return crud.patch_blog(db=db, blog_id=blog_id, blog=blog)

# Удаление блога
@router.delete("/{user_id}/blogs/{blog_id}", response_model=schemas.Blog)
def delete_blog(user_id: int, blog_id: int, db: Session = Depends(get_session)):
    db_blog = crud.get_blog(db, blog_id=blog_id, user_id=user_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Блог не найден")
    return crud.delete_blog(db=db, blog_id=blog_id)