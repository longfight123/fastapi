from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    print(type(item_dict))
    return type(item_dict)