from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.food.get_food_use_case import GetFoodUseCase
from src.domain.models import MealFood
from src.domain.schemas import MealFoodCreate
from src.infrastructure.repositories.diet_repository import diet_repository


class AddFoodToMealUseCase(BaseUseCase[Optional[MealFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository
        self.get_food_use_case = GetFoodUseCase(db)

    def execute(self, meal_plan_id: int, food_in: MealFoodCreate) -> Optional[MealFood]:
        food = self.get_food_use_case.execute(food_in.food_id)
        if not food:
            return None

        return self.diet_repository.add_food_to_meal(
            self.db,
            meal_plan_id=meal_plan_id,
            food_id=food_in.food_id,
            quantity=food_in.quantity,
        )
