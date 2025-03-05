from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Food
from infrastructure.repositories.food_repository import food_repository
from sqlalchemy.orm import Session


class GetFoodByNameUseCase(BaseUseCase[Optional[Food]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.food_repository = food_repository

    def execute(self, name: str) -> Optional[Food]:
        return self.food_repository.get_by_name(self.db, name=name)
