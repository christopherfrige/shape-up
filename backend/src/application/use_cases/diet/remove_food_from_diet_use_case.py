from application.use_cases.base_use_case import BaseUseCase
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class RemoveFoodFromDietUseCase(BaseUseCase[bool]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int, food_id: int) -> bool:
        return self.diet_repository.remove_food(
            self.db, diet_id=diet_id, food_id=food_id
        )
