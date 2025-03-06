from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutPlan


class ListPlansUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[WorkoutPlan]:
        return self.session.query(WorkoutPlan).offset(skip).limit(limit).all()
