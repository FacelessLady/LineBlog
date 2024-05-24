from sqlalchemy.orm import Session
from app import schemas
from app import models

# User CRUD Operations

#Получаем пользователя по его идентификатору в базе данных.
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#Получаем пользователя по его электронной почте.
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#Возвращаем список пользователей с возможностью задать смещение и ограничение количества возвращаемых записей.
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

#Создаем нового пользователя с указанными данными.
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Обновляем данные пользователя.
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

#Частичное обновление данных пользователя.
def patch_user(db: Session, user_id: int, user: schemas.UserUpdate):
    return update_user(db, user_id, user)

#Удаляем пользователя из базы данных.
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Blog CRUD Operations

#Получаем блог по его идентификатору и идентификатору автора.
def get_blog(db: Session, blog_id: int, user_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id, models.Blog.author_id == user_id).first()

#Создаем новый блог с указанными данными и идентификатором автора.
def create_blog(db: Session, blog: schemas.BlogCreate, user_id: int):
    db_blog = models.Blog(**blog.dict(), author_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

#Возвращаем список блогов, принадлежащих определенному пользователю, с возможностью задать смещение и ограничение количества возвращаемых записей.
def get_blogs_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).filter(models.Blog.author_id == user_id).offset(skip).limit(limit).all()

#Обновляем данные блога.
def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    db_blog = get_blog(db, blog_id=blog_id, user_id=blog.author_id)
    if db_blog:
        update_data = blog.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_blog, key, value)
        db.commit()
        db.refresh(db_blog)
    return db_blog

#Осуществляем частичное обновление данных блога.
def patch_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    return update_blog(db, blog_id, blog)

#Удаляем блог из базы данных.
def delete_blog(db: Session, blog_id: int, user_id: int):
    db_blog = get_blog(db, blog_id=blog_id, user_id=user_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog