from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Diet
from src.infrastructure.repositories.diet_repository import diet_repository


class GetDietsByUserUseCase(BaseUseCase[List[Diet]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Diet]:
        return self.diet_repository.get_by_user(self.db, user_id=user_id, skip=skip, limit=limit)
