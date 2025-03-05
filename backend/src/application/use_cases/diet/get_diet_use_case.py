from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Diet
from infrastructure.repositories.diet_repository import diet_repository
from sqlalchemy.orm import Session


class GetDietUseCase(BaseUseCase[Optional[Diet]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int) -> Optional[Diet]:
        return self.diet_repository.get(self.db, id=diet_id)
