from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Food
from src.domain.schemas import FoodUpdate
from src.infrastructure.repositories.food_repository import food_repository


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
