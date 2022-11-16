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

@app.post("/files")
async def create_file(file: bytes | None = File(default=None)):
    if file:
        return {"file_size": len(file)}
    else:
        return {"file_size": "No file sent."}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile | None = None):
    if file:
        return {"filename": file.filename}
    else:
        return {"filename": "No upload file sent."}