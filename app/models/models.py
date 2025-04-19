from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

# Association table for many-to-many relationship between users and movies
user_movie_association = Table(
    'watches',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('watch_date', DateTime, default=datetime.utcnow),
    Column('watch_duration', Integer)  # in minutes
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    
    # Relationships
    watched_movies = relationship("Movie", secondary=user_movie_association, back_populates="watched_by")
    preferences = relationship("Preference", back_populates="user")

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(String)
    year = Column(Integer)
    imdb_rating = Column(Float)
    
    # Relationships
    watched_by = relationship("User", secondary=user_movie_association, back_populates="watched_movies")

class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    genre = Column(String)
    rating = Column(Float)
    
    # Relationships
    user = relationship("User", back_populates="preferences") 