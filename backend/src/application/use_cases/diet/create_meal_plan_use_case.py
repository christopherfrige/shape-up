from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import MealPlan
from src.domain.schemas import MealPlanCreate
from src.infrastructure.repositories.diet_repository import diet_repository


class CreateMealPlanUseCase(BaseUseCase[Optional[MealPlan]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int, meal_plan_in: MealPlanCreate) -> Optional[MealPlan]:
        diet = self.diet_repository.get(self.db, id=diet_id)
        if not diet:
            return None

        return self.diet_repository.create_meal_plan(
            self.db,
            diet_id=diet_id,
            day_of_week=meal_plan_in.day_of_week,
            meal_type=meal_plan_in.meal_type,
        )
