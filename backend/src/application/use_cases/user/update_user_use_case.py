from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import User
from domain.schemas import UserUpdate
from infrastructure.repositories.user_repository import user_repository
from sqlalchemy.orm import Session


class UpdateUserUseCase(BaseUseCase[Optional[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.user_repository = user_repository

    def execute(self, user_id: int, user_in: UserUpdate) -> Optional[User]:
        user = self.user_repository.get(self.db, id=user_id)
        if not user:
            return None
        return self.user_repository.update(
            self.db, db_obj=user, obj_in=user_in.model_dump(exclude_unset=True)
        )
