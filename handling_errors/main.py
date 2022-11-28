from fastapi import FastAPI, HTTPException

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

@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id in items:
        return {"item": items[item_id]}
    else:
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            headers={"x-custom-header": "custom value"}
        )