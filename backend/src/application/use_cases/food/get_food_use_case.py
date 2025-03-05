from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Food
from infrastructure.repositories.food_repository import food_repository
from sqlalchemy.orm import Session


class GetFoodUseCase(BaseUseCase[Optional[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(self, food_id: int) -> Optional[Food]:
        return self.food_repository.get(self.db, id=food_id)
