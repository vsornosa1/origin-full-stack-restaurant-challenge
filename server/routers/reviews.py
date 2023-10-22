from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from server.utils import get_db
from server.crud.reviews import get_reviews_by_plate_id, get_review_by_user_and_plate, create_review
from server.routers.token import get_current_user
from typing import List


router = APIRouter()


@router.get("plates/{plate_id}/", response_model=List[schemas.Review])
def list_reviews_for_plate(plate_id: int, db: Session = Depends(get_db)):
    return get_reviews_by_plate_id(db, plate_id=plate_id)


@router.post("", response_model=schemas.Review)
def create_review_for_plate(
    review: schemas.ReviewCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    existing_review = get_review_by_user_and_plate(db, user_id=current_user.id, plate_id=review.plate_id)
    if existing_review:
        raise HTTPException(status_code=400, detail="Too many! A review has already been provided for this meal.")
    return create_review(db=db, review=review, user_id=current_user.id)
