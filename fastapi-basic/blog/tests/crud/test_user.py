from sqlalchemy.orm import Session

from blog.repository import user
from blog.schemas import User
from blog.tests.utils.utils import random_email, random_lower_string


def test_create_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = User(email=email, password=password)
    new_user = user.create()
    assert new_user.email == email
    assert hasattr(new_user, "hashed_password")
