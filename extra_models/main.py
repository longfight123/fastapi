from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Multiple models

# class UserIn(BaseModel):
#     name: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     name: str
#     email: EmailStr
#     full_name: str | None = None

# class UserDB(BaseModel):
#     name: str
#     email: EmailStr
#     hashed_password: str
#     full_name: str | None = None

# def fake_password_hasher(user: UserIn):
#     return "supersecret" + user.password

# def fake_save_user(user: UserIn):
#     hashed_password = fake_password_hasher(user)
#     user_in_db = UserDB(**user.dict(), hashed_password=hashed_password)
#     print("Saving " + user_in_db.name + " to database")
#     return user_in_db

# @app.post("/user", response_model=UserOut, response_model_exclude_unset=True)
# async def create_user(user: UserIn):
#     user_saved = fake_save_user(user)
#     return user_saved



# Hierarchy of multiple models

# class UserBase(BaseModel):
#     name: str
#     email: EmailStr
#     full_name: str | None = None

# class UserIn(UserBase):
#     password: str

# class UserOut(UserBase):
#     pass

# class UserDB(UserBase):
#     hashed_password: str

# def fake_password_hasher(user: UserIn):
#     return "supersecret" + user.password

# def fake_save_user(user: UserIn):
#     hashed_password = fake_password_hasher(user)
#     user_in_db = UserDB(**user.dict(), hashed_password=hashed_password)
#     print("Saving " + user_in_db.name + " to database")
#     return user_in_db

# @app.post("/user", response_model=UserOut, response_model_exclude_unset=True)
# async def create_user(user: UserIn):
#     user_saved = fake_save_user(user)
#     return user_saved




# Union or anyOf

# from typing import Union

# class BaseItem(BaseModel):
#     description: str
#     type: str

# class CarItem(BaseItem):
#     type = "car"

# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int

# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]




# List of models

class Item(BaseModel):
    name: str
    description: str

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"}
]

@app.get("/items/", response_model=list[Item])
async def read_items():
    return items