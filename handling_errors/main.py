from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

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

# class UnicornException(Exception):

#     def __init__(self, name: str):
#         self.name = name

# @app.exception_handler(UnicornException)
# def unicorn_exception_handler(request: Request, exception: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exception.name} did something."}
#     )

# @app.get("/unicorns/{name}")
# def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# override request validation handlers and HTTPException handlers

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    return PlainTextResponse(
        status_code=422,
        content=str(exception)
    )

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exception: HTTPException):
    return PlainTextResponse(
        status_code=exception.status_code,
        content=exception.detail
    )

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}