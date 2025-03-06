from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import DietFood
from src.infrastructure.repositories.diet_repository import diet_repository


class GetDietFoodsUseCase(BaseUseCase[List[DietFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int) -> List[DietFood]:
        return self.diet_repository.get_foods(self.db, diet_id=diet_id)
