from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import MealFood
from src.infrastructure.repositories.diet_repository import diet_repository


class GetMealFoodsUseCase(BaseUseCase[List[MealFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, meal_plan_id: int) -> List[MealFood]:
        return self.diet_repository.get_meal_foods(self.db, meal_plan_id=meal_plan_id)
