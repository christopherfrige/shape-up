from typing import Optional

from sqlalchemy.orm import Session

from src.domain.models import User
from src.infrastructure.auth import get_password_hash
from src.infrastructure.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: dict) -> User:
        db_obj = User(
            email=obj_in["email"],
            hashed_password=get_password_hash(obj_in["password"]),
            full_name=obj_in["full_name"],
            age=obj_in["age"],
            weight=obj_in["weight"],
            height=obj_in["height"],
            gender=obj_in["gender"],
            activity_level=obj_in["activity_level"],
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: User, obj_in: dict) -> User:
        update_data = obj_in.copy()
        if "password" in update_data:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)


user_repository = UserRepository(User)
