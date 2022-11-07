from fastapi import FastAPI, Path, Query

app = FastAPI()


# Path parameter with meta data
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(title="The ID of the item to get"),
#     q: str | None = Query(default=None, alias="item-query")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Parameters in any order that we need, even default values before parameters without default values
# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: int = Path(title="The ID of the item to get"),
#     q: str | None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Number validations in any parameter
# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=1),
#     q: str | None
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# gt, lt, ge, le
@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=1, le=1000),
    q: float | None = Query(gt=0, lt=1.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results