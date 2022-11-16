from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Use File and UploadFile. File is necessary to specify that the parameter should be a File body, not a 
# Query parameter or a Body Parameter. 
# If you declare the parameter type to be bytes, FastAPI will read the file for you and you will receive the
# contents as bytes.

# @app.post("/files")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}

# # Use await file.read() if inside of a async function
# # Use file.file.read() if inside of a normal def function

# @app.post("/uploadfile")
# async def create_upload_file(file: UploadFile):
#     print(await file.read())
#     return {"filename": file.filename}



# Make a file optional by using type annotation and default=None

# @app.post("/files")
# async def create_file(file: bytes | None = File(default=None)):
#     if file:
#         return {"file_size": len(file)}
#     else:
#         return {"file_size": "No file sent."}

# @app.post("/uploadfile")
# async def create_upload_file(file: UploadFile | None = None):
#     if file:
#         return {"filename": file.filename}
#     else:
#         return {"filename": "No upload file sent."}




# Add metadata with UploadFile by using the File() class/function

# @app.post("/files")
# async def create_file(file: bytes | None = File(default=None, description="A file read as bytes")):
#     if file:
#         return {"file_size": len(file)}
#     else:
#         return {"file_size": "No file sent."}

# @app.post("/uploadfile")
# async def create_upload_file(file: UploadFile | None = File(default=None, description="A file read as UploadFile")):
#     if file:
#         return {"filename": file.filename}
#     else:
#         return {"filename": "No upload file sent."}



# Declaring multiple File Uploads

from fastapi.responses import HTMLResponse

@app.post("/files")
async def create_file(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles")
async def create_upload_file(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)