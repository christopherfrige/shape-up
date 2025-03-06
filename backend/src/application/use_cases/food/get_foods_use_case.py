from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Food
from src.infrastructure.repositories.food_repository import food_repository


class GetFoodsUseCase(BaseUseCase[List[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(self, skip: int = 0, limit: int = 100) -> List[Food]:
        return self.food_repository.get_multi(self.db, skip=skip, limit=limit)
