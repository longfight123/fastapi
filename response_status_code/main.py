from fastapi import FastAPI, status

app = FastAPI()

# Setting a status code for the response

@app.post("/items/", status_code=201)
async def read_items(name: str):
    return {"name": name}





# Using the convenience variables in fastapi.status instead of memorizing the codes

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def read_items(name: str):
    return {"name": name}