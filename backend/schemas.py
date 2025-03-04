from pydantic import BaseModel, EmailStr
from typing import Optional

class UsersBase(BaseModel):
    name: str
    email: str

class UsersCreate(UsersBase):
    password: str

class UserResponse(UsersBase):
    id: int
    password: str

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    UserId: int
    title: str
    description: Optional[str]=None
    completed: bool=False


class TaskResponse(TaskBase):
    id: int
    class Config:
        from_attributes = True