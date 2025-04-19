from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base, User, Movie, Preference
from datetime import datetime
from faker import Faker
import random
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:your_password@localhost:5432/NetflixRecommendation")
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Initialize Faker
fake = Faker()

# Movie genres
genres = [
    "Action", "Adventure", "Animation", "Biography", "Comedy",
    "Crime", "Documentary", "Drama", "Family", "Fantasy",
    "Film-Noir", "History", "Horror", "Music", "Musical",
    "Mystery", "Romance", "Sci-Fi", "Sport", "Thriller",
    "War", "Western"
]

# Generate 100 movies
movies = []
for _ in range(100):
    year = random.randint(1970, 2024)
    rating = round(random.uniform(5.0, 9.9), 1)
    genre = random.choice(genres)
    movie = Movie(
        name=fake.unique.catch_phrase(),
        genre=genre,
        year=year,
        imdb_rating=rating
    )
    movies.append(movie)

# Generate 1000 users
users = []
for _ in range(1000):
    age = random.randint(18, 80)
    gender = random.choice(["Male", "Female"])
    user = User(
        name=fake.name(),
        email=fake.unique.email(),
        age=age,
        gender=gender
    )
    users.append(user)

# Generate user preferences (3-5 preferences per user)
preferences = []
for user_id in range(1, 1001):
    num_preferences = random.randint(3, 5)
    user_genres = random.sample(genres, num_preferences)
    for genre in user_genres:
        preference = Preference(
            user_id=user_id,
            genre=genre,
            rating=round(random.uniform(1.0, 5.0), 1)
        )
        preferences.append(preference)

try:
    # Add movies
    print("Adding movies...")
    for movie in movies:
        db.add(movie)
    db.commit()

    # Add users
    print("Adding users...")
    for user in users:
        db.add(user)
    db.commit()

    # Add preferences
    print("Adding preferences...")
    for preference in preferences:
        db.add(preference)
    db.commit()

    # Add watching records (10-20 movies per user)
    print("Adding watching records...")
    for user in users:
        num_movies = random.randint(10, 20)
        watched_movies = random.sample(movies, num_movies)
        user.watched_movies.extend(watched_movies)
        db.commit()

    print("Database created successfully with sample data!")
    print(f"Total users: {len(users)}")
    print(f"Total movies: {len(movies)}")
    print(f"Total preferences: {len(preferences)}")
    print("Average movies watched per user: 15")

except Exception as e:
    db.rollback()
    print(f"An error occurred: {e}")
finally:
    db.close() 