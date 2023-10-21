from datetime import datetime
from typing import List, Optional, Any

from pydantic.utils import GetterDict
from pydantic import BaseModel


# PLATES ========================
class PlateBase(BaseModel):
    plate_name: str
    price: float
    picture: Optional[str] = None


class Plate(PlateBase):
    plate_id: int

    class Config:
        orm_mode = True


class PlateCount(Plate):
    order_count: int

    class Config:
        orm_mode = True


class PlateOrderBase(BaseModel):
    plate_id: int
    quantity: int


class PlateOrderGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {'plate_name'}:
            return getattr(self._obj.plate, key)
        else:
            return super(PlateOrderGetter, self).get(key, default)


class PlateOrder(PlateOrderBase):
    plate_name: str
    class Config:
        orm_mode = True
        getter_dict = PlateOrderGetter


# ORDERS ========================
class OrderBase(BaseModel):
    user_id: int
    plates: List[PlateOrderBase]
    

class Order(OrderBase):   
    order_id: int
    order_time: datetime
    plates: List[PlateOrder]

    class Config:
        orm_mode = True

# USERS ========================
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Sent back after 200 auth
class Token(BaseModel):
    access_token: str     # JWT string
    token_type: str       # 'bearer' type of token

class TokenData(BaseModel):
    username: str
    password: str