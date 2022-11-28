from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

# response status_code

# @app.post("/items/", response_model=Item, status_code=status.HTTP_200_OK)
# async def create_item(item: Item):
#     return item

# Tags

@app.post("/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item

@app.get("/items/", response_model=Item, tags=["items"])
async def get_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=["users"])
async def get_users():
    return [{"username": "johndoe"}]