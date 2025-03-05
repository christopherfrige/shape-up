from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import MealFood
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class GetMealFoodsUseCase(BaseUseCase[List[MealFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, meal_plan_id: int) -> List[MealFood]:
        return self.diet_repository.get_meal_foods(self.db, meal_plan_id=meal_plan_id)
