from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_plan import WorkoutPlan
from sqlalchemy.orm import Session


class ListPlansUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[WorkoutPlan]:
        return self.session.query(WorkoutPlan).offset(skip).limit(limit).all()
