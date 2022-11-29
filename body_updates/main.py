from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     items[item_id] = jsonable_encoder(item)
#     print(items[item_id])
#     return items[item_id]

# Use patch and dict(exclude_unset) and pydantic models model.copy(update=update_model)
# to copy over any attributes from update_model to model. Only copies the attributes
# that were explicitly set in update_model and leaves the rest as is

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item = item.dict(exclude_unset=True)
    saved_item = items[item_id]
    saved_item_model = Item(**saved_item)
    saved_item_model = saved_item_model.copy(update=update_item)
    items[item_id] = jsonable_encoder(saved_item_model)
    return saved_item_model
