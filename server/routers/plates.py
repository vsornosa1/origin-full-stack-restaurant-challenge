from fastapi import APIRouter, Depends, HTTPException
from typing import List

from server.crud.plates import get_plates, add_plate, get_plates_count, get_avg_rating_by_plate_id
from server.schemas import PlateBase, Plate, PlateCount
from server.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()




@router.get("/average/{plate_id}", response_model=float)
def get_average_rating(plate_id: int, db: Session = Depends(get_db)):
    avg_rating = get_avg_rating_by_plate_id(db, plate_id)
    if avg_rating is None:
        raise HTTPException(status_code=404, detail="Meal not found or no ratings available.")
    return avg_rating



@router.get("", response_model=List[Plate])
async def search_plates(db_session: Session = Depends(get_db)):
    """Find Plates.

    """
    return get_plates(db_session)


@router.get("/ranking", response_model=List[PlateCount])
async def search_plates_count(db_session: Session = Depends(get_db)):
    """Find the ranked order of plates"""
    return get_plates_count(db_session)


@router.post("", response_model=Plate)
async def post_new_plate(
    item: PlateBase,
    db_session: Session = Depends(get_db),
):
    """Find order by ID.

    """
    return add_plate(db_session, item)


