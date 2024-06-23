from pydantic import BaseModel,EmailStr,Field
from datetime import datetime,timedelta
from typing import Optional

class PostBase(BaseModel):
    title:str=Field(description="Title of post",min_length=3,max_length=40)
    content:str=Field(description="Content of the post",min_length=10,max_length=300)
    published:bool=Field(description="Is the post published ",default=True)

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)