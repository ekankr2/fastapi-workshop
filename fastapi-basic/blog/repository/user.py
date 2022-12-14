from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash

from .. import schemas, models
from ..models.user import User


def create(request: schemas.User, db: Session):
    new_user = User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")

    return user
