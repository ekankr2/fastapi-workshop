from sqlalchemy.orm import declarative_base

Base = declarative_base()
from blog.models.user import User
from blog.models.blog import Blog
from blog.models.image import Image
