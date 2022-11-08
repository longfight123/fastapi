from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

# Declare the type of list in Python 3.11
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(default=None, title="The description of the item", max_length=300)
#     price: float
#     tax: float | None = Field(default=None, description="The price must be greater than 0", gt=0)
#     tags: list[str] = []

# Declare a list field in the model
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     item: Item
# ):
#     results = {"item_id": item_id}
#     results.update({"item": item})
#     return results




# Declare a submodel Image
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# Declare the type of set in Python 3.11
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(default=None, title="The description of the item", max_length=300)
#     price: float
#     tax: float | None = Field(default=None, description="The price must be greater than 0", gt=0)
#     tags: set[str] = set()
#     image: Image | None = None

# Declare a list field in the model
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     item: Item
# ):
#     results = {"item_id": item_id}
#     results.update({"item": item})
#     return results




# Declare a submodel Image
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# Declare a list of submodels
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(default=None, title="The description of the item", max_length=300)
#     price: float
#     tax: float | None = Field(default=None, description="The price must be greater than 0", gt=0)
#     tags: set[str] = set()
#     images: list[Image] | None = None

# Declare a list field in the model
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     item: Item
# ):
#     results = {"item_id": item_id}
#     results.update({"item": item})
#     return results



# Deeply Nested Models

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float
    tax: float | None = Field(default=None, description="The price must be greater than 0", gt=0)
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.put("/offers")
async def update_item(*,  offer: Offer):
    return offer


# Bodies of pure lists

@app.post("/images/multiple")
async def create_multiple_images(images: list[Image]):
    return images