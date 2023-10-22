from sqlalchemy.orm import Session
from .. import models, schemas


def get_reviews_by_plate_id(db: Session, plate_id: int):
    print(plate_id)
    return db.query(models.Review).filter(models.Review.plate_id == plate_id).all()

def get_review_by_user_and_plate(db: Session, user_id: int, plate_id: int):
    return db.query(models.Review).filter(models.Review.user_id == user_id, models.Review.plate_id == plate_id).first()


def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(**review.dict(), user_id=user_id) #**=AttrSegmentation
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
