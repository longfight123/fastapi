import models
import schemas

from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user

def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "fake_hash"
    new_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_items(db: Session, skip: int = 0, limit: int = 100):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

def create_user_item(db: Session, user_id: int, item: schemas.ItemCreate):
    db_item = models.Item(title = item.title, description = item.description, owner_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
