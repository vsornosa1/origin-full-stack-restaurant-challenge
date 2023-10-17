from sqlalchemy.orm import Session
from server.schemas import UserCreate
import server.models as md
import bcrypt


def get_user_by_username(db: Session, username: str):
    return db.query(md.User).filter(md.User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = md.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_password_hash(password: str) -> str:
    password_encoded = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_encoded, bcrypt.gensalt())
    return hashed.decode('utf-8')  # Hashed bytes -> string (to db)

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


