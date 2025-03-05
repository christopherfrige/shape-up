from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import DietFood
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class GetDietFoodsUseCase(BaseUseCase[List[DietFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int) -> List[DietFood]:
        return self.diet_repository.get_foods(self.db, diet_id=diet_id)
