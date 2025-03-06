from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Diet
from src.infrastructure.repositories.diet_repository import diet_repository


class GetDietUseCase(BaseUseCase[Optional[Diet]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int) -> Optional[Diet]:
        return self.diet_repository.get(self.db, id=diet_id)
