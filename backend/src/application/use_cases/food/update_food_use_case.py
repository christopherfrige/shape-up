from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Food
from domain.schemas import FoodUpdate
from infrastructure.repositories.food_repository import food_repository
from sqlalchemy.orm import Session


class UpdateFoodUseCase(BaseUseCase[Optional[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(self, food_id: int, food_in: FoodUpdate) -> Optional[Food]:
        food = self.food_repository.get(self.db, id=food_id)
        if not food:
            return None
        return self.food_repository.update(
            self.db, db_obj=food, obj_in=food_in.model_dump(exclude_unset=True)
        )
