from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float
    tax: float | None = Field(default=None, description="The price must be greater than 0", gt=0)

# Use the Field() class to declare extra validation and metadata for pydantic models
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    item: Item = Body(embed=True),
):
    results = {"item_id": item_id}
    results.update({"item": item})
    return results