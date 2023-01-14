from pydantic import BaseModel, Field, EmailStr

from src.constants import USERNAME_LENGTH


class UserModel(BaseModel):
    username: str = Field(max_length=USERNAME_LENGTH)
    email: str = EmailStr()
    password: str = Field(max_length=8, min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    class Config:
        orm_mode = True

