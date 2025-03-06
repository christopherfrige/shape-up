from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import MealPlan


class ListMealPlansUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[MealPlan]:
        return self.session.query(MealPlan).offset(skip).limit(limit).all()
