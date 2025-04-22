# Netflix-Style Movie Recommendation System

## Contributors
Tuba SARIKAYA & Gül ERTEN -- GYK1

## Overview
This project implements a sophisticated movie recommendation system similar to Netflix, using machine learning algorithms to provide personalized movie suggestions based on user preferences and viewing history. The system is built with FastAPI for the backend, PostgreSQL for data storage, and implements the KMeans clustering algorithm for generating recommendations.

## Features
- User management system
- Comprehensive movie database
- User preference tracking
- Viewing history management
- Genre-based recommendations
- Machine learning-powered suggestion engine
- RESTful API with Swagger documentation

## Technical Stack
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Machine Learning:** scikit-learn (KMeans clustering)
- **Data Processing:** Pandas, NumPy
- **Documentation:** Swagger/OpenAPI
- **Development Tools:** Python 3.8+

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)

### Setup Steps

1. Clone the repository:
```bash
git clone [repository-url]
cd netflix_recommendation_system
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL database:
```sql
CREATE DATABASE "NetflixRecommendation";
```

4. Configure database connection:
Create a `.env` file in the project root with the following content:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/NetflixRecommendation
```

5. Initialize the database with sample data:
```bash
python create_database.py
```
This will create:
- 1000 sample users
- 100 movies
- 3-5 genre preferences per user
- 10-20 watched movies per user

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload --port 8001
```

2. Access the API documentation:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

## API Endpoints

### User Management
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get user details
- `POST /users/create` - Create new user
- `GET /users/{user_id}/preferences` - Get user preferences
- `GET /users/{user_id}/watched-movies` - Get user's watch history

### Movie Management
- `GET /movies/` - List all movies
- `GET /movies/{movie_id}` - Get movie details
- `POST /movies/watch/save` - Record movie watch event

### Recommendations
- `GET /recommendations/{user_id}` - Get personalized movie recommendations

## Data Structure

### Users
- ID
- Name
- Email
- Age
- Gender
- Watch History
- Genre Preferences

### Movies
- ID
- Name
- Genre
- Year
- IMDB Rating

### Preferences
- User ID
- Genre
- Rating

## Machine Learning Implementation
The system uses KMeans clustering to group users based on their:
- Genre preferences
- Watch history
- Age demographics
- Rating patterns

## Testing
To test the API using Swagger UI:
1. Navigate to http://localhost:8001/docs
2. Try out different endpoints
3. Use sample user IDs (1-1000)
4. Explore movie recommendations
5. Test user preferences and watch history

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
