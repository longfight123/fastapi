from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

# Declaring path, query, and body parameters
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     q: str | None = None,
#     item: Item | None = None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

# Declaring path, query, and body parameters
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     user: User,
#     item: Item
# ):
#     results = {"item_id": item_id}
#     results.update({"item": item})
#     results.update({"user": user})
#     return results

# Declaring a singular value in the body
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    user: User,
    item: Item,
    importance: int = Body()
):
    results = {"item_id": item_id}
    results.update({"item": item})
    results.update({"user": user})
    results.update({"importance": importance})
    return results