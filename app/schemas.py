from pydantic import BaseModel
from typing import List, Optional
import datetime

class BlogBase(BaseModel):
    title: str
    content: str
    is_active: bool = False

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_superuser: bool = False
    blogs: List[Blog] = []

    class Config:
        orm_mode = True