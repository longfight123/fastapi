from fastapi import FastAPI, Header

app = FastAPI()


# user_agent is a predefined header and will take on the value of the header sent by the browser

# @app.get("/items")
# async def read_items(user_agent: str | None = Header(default=None)):
#     return {"User-Agent": user_agent}


# defining a different non predefined header with convert_underscores=False

@app.get("/items")
async def read_items(strange_header: str | None = Header(default=None, convert_underscores=False)):
    return {"strange_header": strange_header}