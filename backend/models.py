from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    mail=Column(String, nullable=False)
    password=Column(String, nullable=False)

    tasks = relationship("Tasks", back_populates="user", cascade="all, delete")

    


class Tasks(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

    user= relationship("Users", back_populates="tasks")
    