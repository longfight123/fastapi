from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Using a response model for data validation purposes

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    return item