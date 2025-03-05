from application.use_cases.base_use_case import BaseUseCase
from domain.models import Diet
from domain.schemas import DietCreate
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class CreateDietUseCase(BaseUseCase[Diet]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_in: DietCreate, user_id: int) -> Diet:
        diet_data = diet_in.model_dump()
        diet_data["user_id"] = user_id
        return self.diet_repository.create(self.db, obj_in=diet_data)
