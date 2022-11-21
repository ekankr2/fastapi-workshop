from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.db.base import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates="images")