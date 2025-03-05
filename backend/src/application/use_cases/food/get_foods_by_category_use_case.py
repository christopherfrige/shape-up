from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Food, FoodCategory
from infrastructure.repositories.food_repository import food_repository
from sqlalchemy.orm import Session


class GetFoodsByCategoryUseCase(BaseUseCase[List[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(
        self, category: FoodCategory, skip: int = 0, limit: int = 100
    ) -> List[Food]:
        return self.food_repository.get_by_category(
            self.db, category=category, skip=skip, limit=limit
        )
