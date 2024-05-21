from pydantic import BaseModel
from typing import List, Optional
import datetime

#базовая модель для блога
class BlogBase(BaseModel):
    title: str
    content: str
    is_active: bool = False

#модель для создания нового блога
class BlogCreate(BlogBase):
    pass

#модель для обновления существующего блога
class BlogUpdate(BlogBase):
    pass

#модель для представления блога
class Blog(BlogBase):
    id: int
    author_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True

#базовая модель для пользователя
class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True

#модель для создания нового пользователя
class UserCreate(UserBase):
    password: str

#модель для обновления существующего пользователя
class UserUpdate(UserBase):
    password: Optional[str] = None

#модель для представления пользователя
class User(UserBase):
    id: int
    is_superuser: bool = False
    blogs: List[Blog] = []

    class Config:
        orm_mode = True