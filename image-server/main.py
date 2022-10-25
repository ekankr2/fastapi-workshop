import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/")
async def root(file: UploadFile = File(...)):
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}


@app.post("/img")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "Good"}
