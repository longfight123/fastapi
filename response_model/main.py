from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Using a response model for data validation purposes

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []

# @app.post("/items", response_model=Item)
# async def create_item(item: Item):
#     return item



# Returning the same input data

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user



