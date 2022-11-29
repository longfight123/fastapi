from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import datetime

app = FastAPI()

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime.datetime
    description: str | None = None

@app.put("/items/{id}")
async def update_item(id: int, item: Item):
#     fake_db[id] = item.dict()
    fake_db[id] = jsonable_encoder(item)
    print(type(jsonable_encoder(item)))
    print(fake_db)

