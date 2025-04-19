from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.models import Film, Kullanici
from ..schemas.schemas import FilmCreate, Film as FilmSchema, IzlemeCreate, Izleme as IzlemeSchema
from datetime import datetime

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

@router.post("/", response_model=MovieSchema)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.get("/", response_model=List[MovieSchema])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = db.query(Movie).offset(skip).limit(limit).all()
    return movies

@router.get("/{movie_id}", response_model=MovieSchema)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/watch/save", response_model=WatchSchema)
def save_watching(watch: WatchCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == watch.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if movie exists
    movie = db.query(Movie).filter(Movie.id == watch.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    # Add movie to user's watched movies
    user.watched_movies.append(movie)
    db.commit()
    
    return WatchSchema(
        id=len(user.watched_movies),
        user_id=user.id,
        movie_id=movie.id,
        watch_date=datetime.utcnow(),
        watch_duration=watch.watch_duration
    ) 