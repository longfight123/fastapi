from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# Declaring an example with Config and schema_extra

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2
#             }
#         }

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": Item}
#     return results



# Declaring an example with Field()

class Item(BaseModel):
    name: str = Field(example="Foo")
    description: str | None = Field(example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": Item}
    return results