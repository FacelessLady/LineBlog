from sqlalchemy import (Column, Integer, Text, String, Boolean, DateTime, ForeignKey)
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db import Base

class Blog(Base):
    id = Column("id", Integer, primary_key=True),
    title = Column("Заголовок", String, nullable=False),
    content = Column("Содержание", Text, nullable=False),
    author__id = Column(Integer, ForeignKey("user.id")),
    author = relationship("Пользователь(User)", back_populates="blogs")
    created_at = Column("Создано в", DateTime, default=datetime.now),
    is_active = Column("Активен", Boolean, default=False)
    
    