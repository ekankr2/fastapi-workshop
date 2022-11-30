from sqlalchemy.orm import Session

from blog.hashing import Hash
from blog.repository import user
from blog.schemas import User
from blog.tests.utils.utils import random_email, random_lower_string


def test_create_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    name = 'ekan'
    user_in = User(email=email, password=Hash.bcrypt(password), name=name)
    new_user = user.create(user_in, db)
    assert new_user.email == email
    assert new_user.name == name