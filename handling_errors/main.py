from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

items = {
    "foo": "The Foo Wrestlers"
}

# @app.get("/items/{item_id}")
# def get_item(item_id: str):
#     if item_id in items:
#         return {"item": items[item_id]}
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")


# Add a custom header

# @app.get("/items/{item_id}")
# def get_item(item_id: str):
#     if item_id in items:
#         return {"item": items[item_id]}
#     else:
#         raise HTTPException(
#             status_code=404, 
#             detail="Item not found",
#             headers={"x-custom-header": "custom value"}
        # )

# Raise custom exceptions

class UnicornException(Exception):

    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
def unicorn_exception_handler(request: Request, exception: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exception.name} did something."}
    )

@app.get("/unicorns/{name}")
def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


