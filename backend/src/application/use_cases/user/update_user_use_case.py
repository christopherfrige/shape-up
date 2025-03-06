from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import User
from src.domain.schemas import UserUpdate
from src.infrastructure.repositories.user_repository import user_repository


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
