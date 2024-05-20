from sqlalchemy.orm import Session
from app import schemas
from app.models import blog_post
from models import users


# User CRUD Operations 
def get_user(db: Session, user_id: int):
    return db.query(users.User).filter(users.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(users.User).filter(users.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = users.User(email=user.email, hashed_password=fake_hashed_password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(users.User).offset(skip).limit(limit).all()


#  Blog CRUD Operations 
def get_blog(db: Session, blog_id: int):
    return db.query(blog_post.Blog).filter(blog_post.Blog.id == blog_id).first()

def create_blog(db: Session, blog: schemas.BlogCreate, user_id: int):
    db_blog = blog_post.Blog(**blog.dict(), author_id=user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(blog_post.Blog).offset(skip).limit(limit).all()

def get_blogs_by_user(db: Session, user_id: int, skip: int =0, limit: int = 10):
   return db.query(blog_post.Blog).filter(blog_post.Blog.author_id == user_id).offset(skip).limit(limit).all()