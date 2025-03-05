from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import User
from infrastructure.repositories.user_repository import user_repository
from sqlalchemy.orm import Session


class GetUsersUseCase(BaseUseCase[List[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.user_repository = user_repository

    def execute(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.user_repository.get_multi(self.db, skip=skip, limit=limit)
