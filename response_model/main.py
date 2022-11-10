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



# Returning a different output model

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user



# Using response_model_exclude_unset=True parameter

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_items(item_id: str):
    return items[item_id]