from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import jwt
import bcrypt
from server.utils import get_db
from server.schemas import TokenData
import server.crud.users as crud
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "cerns3cr3tr3st4ur4nt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("")
def login_for_access_token(form_data: TokenData, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        print('🚗🚗ERROR2')
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}