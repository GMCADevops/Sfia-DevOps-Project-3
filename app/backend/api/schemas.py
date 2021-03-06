from typing import List, Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre:str
    rating:int
    release:int


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
    owner_id: str
    movie_created_at:str
    movieImage : Optional[str] = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name   : Optional[str] = None
    gender      : Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserUpdateImage(UserBase):
    userImage: Optional[str] = None
class User(UserBase):
    id: Optional[str] = None
    is_active: Optional[bool] = None
    created_at  : Optional[str] = None
    hashed_password: Optional[str] = None
    is_active_email : Optional[bool] = None
    userType : Optional[str] = None
    userImage : Optional[str] = None
    movies: List[Movie] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None