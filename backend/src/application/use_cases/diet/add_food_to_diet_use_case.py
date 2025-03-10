from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.food.get_food_use_case import GetFoodUseCase
from src.domain.models import DietFood
from src.domain.schemas import DietFoodCreate
from src.infrastructure.repositories.diet_repository import diet_repository


class AddFoodToDietUseCase(BaseUseCase[Optional[DietFood]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository
        self.get_food_use_case = GetFoodUseCase(db)

    def execute(self, diet_id: int, food_in: DietFoodCreate) -> Optional[DietFood]:
        diet = self.diet_repository.get(self.db, id=diet_id)
        if not diet:
            return None

        food = self.get_food_use_case.execute(food_in.food_id)
        if not food:
            return None

        return self.diet_repository.add_food(
            self.db, diet_id=diet_id, food_id=food_in.food_id, quantity=food_in.quantity
        )
