from fastapi import FastAPI, Query

app = FastAPI()

# Using Query for more validation
# @app.get("/items")
# async def read_items(q: str | None = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Using query with regex
# @app.get("/items")
# async def read_items(q: str | None = Query(default=None, max_length=50, regex="^fixedquery$")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Using Query to require a list of values as a query parameter
@app.get("/items")
async def read_items(q: list[str] | None = Query(default=None, max_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Using Query and adding metadata to the query parameter
@app.get("/items")
async def read_items(q: list[str] | None = Query(
    default=None, 
    title="Query string", 
    description="Query string for items to search in database", 
    max_length=3
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results