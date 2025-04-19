from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.recommendation_service import RecommendationService
from ..schemas.schemas import RecommendationResponse

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.get("/{user_id}", response_model=List[RecommendationResponse])
def get_recommendations(user_id: int, limit: int = 10, db: Session = Depends(get_db)):
    recommendation_service = RecommendationService(db)
    recommendations = recommendation_service.get_recommendations(user_id, limit)
    
    if not recommendations:
        raise HTTPException(
            status_code=404,
            detail="No recommendations found for user or user does not exist"
        )
    
    return recommendations 