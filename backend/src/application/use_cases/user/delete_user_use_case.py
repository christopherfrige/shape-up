from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import User
from infrastructure.repositories.user_repository import user_repository
from sqlalchemy.orm import Session


class DeleteUserUseCase(BaseUseCase[Optional[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.user_repository = user_repository

    def execute(self, user_id: int) -> Optional[User]:
        return self.user_repository.delete(self.db, id=user_id)
