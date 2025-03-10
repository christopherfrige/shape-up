from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Diet
from src.domain.schemas import DietUpdate
from src.infrastructure.repositories.diet_repository import diet_repository


class UpdateDietUseCase(BaseUseCase[Optional[Diet]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.diet_repository = diet_repository

    def execute(self, diet_id: int, diet_in: DietUpdate) -> Optional[Diet]:
        diet = self.diet_repository.get(self.db, id=diet_id)
        if not diet:
            return None
        return self.diet_repository.update(
            self.db, db_obj=diet, obj_in=diet_in.model_dump(exclude_unset=True)
        )
