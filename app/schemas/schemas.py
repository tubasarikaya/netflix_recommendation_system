from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PreferenceBase(BaseModel):
    genre: str
    rating: float

class PreferenceCreate(PreferenceBase):
    pass

class Preference(PreferenceBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str
    email: str
    age: int
    gender: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    preferences: List[Preference] = []

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    name: str
    genre: str
    year: int
    imdb_rating: float

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True

class WatchBase(BaseModel):
    user_id: int
    movie_id: int
    watch_duration: int

class WatchCreate(WatchBase):
    pass

class Watch(WatchBase):
    id: int
    watch_date: datetime

    class Config:
        from_attributes = True

class RecommendationResponse(BaseModel):
    movie_id: int
    movie_name: str
    genre: str
    year: int
    imdb_rating: float
    similarity_score: float 