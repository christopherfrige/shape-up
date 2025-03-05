from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import MealPlan
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class GetMealPlansUseCase(BaseUseCase[List[MealPlan]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int) -> List[MealPlan]:
        return self.diet_repository.get_meal_plans(self.db, diet_id=diet_id)
