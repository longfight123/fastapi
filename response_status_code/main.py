from fastapi import FastAPI

app = FastAPI()

# Setting a status code for the response

@app.post("/items/", status_code=201)
async def read_items(name: str):
    return {"name": name}