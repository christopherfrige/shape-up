from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models.meal_plan import MealPlan
from sqlalchemy.orm import Session


class ListMealPlansUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[MealPlan]:
        return self.session.query(MealPlan).offset(skip).limit(limit).all()
