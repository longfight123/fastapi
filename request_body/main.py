from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# Getting request body in function
@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * item.tax
        item_dict["price_with_tax"] = price_with_tax
    return item_dict

# Post request body with path parameters
@app.post("/items/{item_id}")
async def create_item_with_path_parameter(item_id: int, item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * item.tax
        item_dict["price_with_tax"] = price_with_tax
    item_dict.update({"item_id": item_id})
    return item_dict

# Post request body with path parameters and query params
@app.post("/items2/{item_id}")
async def create_item_with_path_and_query_parameter(item_id: int, item: Item, q: str | None = None):
    item_dict = item.dict()
    item_dict.update({"item_id": item_id})
    if item.tax:
        price_with_tax = item.price * item.tax
        item_dict["price_with_tax"] = price_with_tax
    if q:
        item_dict.update({"q": q})
    return item_dict