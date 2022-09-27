from fastapi import FastAPI
from . import schemas, models
from blog.schemas import Blog
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: Blog):
    return request
