from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Базовая модель для блога
class BlogBase(BaseModel):
    title: str
    content: str
    is_active: Optional[bool] = True

# Модель для создания нового блога
class BlogCreate(BlogBase):
    pass

# Модель для обновления существующего блога
class BlogUpdate(BlogBase):
    author_id: int

    class Config:
        orm_mode = True

# Модель для представления блога
class Blog(BlogBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Базовая модель для пользователя
class UserBase(BaseModel):
    name: str
    email: str

# Модель для создания нового пользователя
class UserCreate(UserBase):
    password: str

# Модель для обновления существующего пользователя
class UserUpdate(UserBase):
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

# Модель для представления пользователя
class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    blogs: List[Blog] = []

    class Config:
        orm_mode = True