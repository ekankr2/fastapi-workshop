from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")
    images = relationship('Image', back_populates="creator")