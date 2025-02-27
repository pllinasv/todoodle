from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Todo(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    mail=Column(String, nullable=False)
    password=Column(String, nullable=False)

    