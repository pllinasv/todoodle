from pydantic import BaseModel, EmailStr
from typing import Optional

class UsersBase(BaseModel):
    name: str
    email: EmailStr


class UsersCreate(UsersBase):
    password: str

class UserResponse(UsersBase):
    id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    userId: int
    title: str[str]
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(UsersBase):
    id: int
    class Config:
        from_attributes = True


