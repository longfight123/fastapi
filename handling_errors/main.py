from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException    
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from pydantic import BaseModel

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

# @app.exception_handler(RequestValidationError)
# def validation_exception_handler(request: Request, exception: RequestValidationError):
#     return PlainTextResponse(
#         status_code=422,
#         content=str(exception)
#     )

# @app.exception_handler(HTTPException)
# def http_exception_handler(request: Request, exception: HTTPException):
#     return PlainTextResponse(
#         status_code=exception.status_code,
#         content=exception.detail
#     )

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}


# Use the RequestValidationError body and error()

# class Item(BaseModel):
#     name: str
#     size: int

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exception: RequestValidationError):
#     return JSONResponse(
#         content=jsonable_encoder({"detail": exception.errors(), "body": exception.body}),
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
#     )

# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# Reuse fastapi's exception handlers

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: RequestValidationError):
    print(f"OMG A VALIDATION ERROR: {repr(exception)}")
    return await request_validation_exception_handler(request, exception)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exception: StarletteHTTPException):
    print(f"OMG! An HTTP Error! {exception}")
    return await http_exception_handler(request, exception)

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}