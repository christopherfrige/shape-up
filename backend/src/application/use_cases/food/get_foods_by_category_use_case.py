from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Food, FoodCategory
from src.infrastructure.repositories.food_repository import food_repository


class GetFoodsByCategoryUseCase(BaseUseCase[List[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(self, category: FoodCategory, skip: int = 0, limit: int = 100) -> List[Food]:
        return self.food_repository.get_by_category(
            self.db, category=category, skip=skip, limit=limit
        )
