from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, movies, recommendations
from .database import engine
from .models import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Netflix Recommendation System",
    description="Movie/Series recommendation system based on user viewing preferences",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(recommendations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Netflix Recommendation System API!"} 