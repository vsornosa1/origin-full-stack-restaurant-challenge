from fastapi import APIRouter, Depends, HTTPException
from server.schemas import OrderBase, Order
from server.crud.orders import get_orders, add_order
from server.utils import get_db
import server.models as md
from sqlalchemy.orm import Session
from typing import List
from server.routers.token import get_current_user


router = APIRouter()


@router.get("", response_model=List[Order])
async def search_orders(db_session: Session = Depends(get_db)):
    return get_orders(db_session)


@router.post("", response_model=Order)
async def add_new_order(
    item: OrderBase,
    current_user: md.User = Depends(get_current_user),
    db_session: Session = Depends(get_db)
):
    try:
        return add_order(db_session, item, current_user.id)
    except Exception as e:
        print(f"🔥 Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))