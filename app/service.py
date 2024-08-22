from sqlalchemy.orm import Session

from . import models, schemas


def create_user(user:schemas.UserCreate, db:Session):
    fake_hashed_password = user.password + "randomletters"
    db_user = models.User(username=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user