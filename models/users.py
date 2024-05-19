from sqlalchemy import (Boolean, Column, Integer, String)
from sqlalchemy.orm import relationship
from public.db import Base


class User(Base):
    id = Column("id", Integer, primary_key=True, index=True),
    email = Column("email", String, nullable=False, unique=True, index=True),
    password = Column("hashed_password", String, nullable=False),
    is_superuser = Column(Boolean(), default=False)
    is_active = Column("is_active", Boolean(), default=True),
    blogs = relationship("Blog", back_populates="author")
