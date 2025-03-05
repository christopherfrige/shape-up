from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_session import WorkoutSession
from sqlalchemy.orm import Session


class ListSessionsUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[WorkoutSession]:
        return self.session.query(WorkoutSession).offset(skip).limit(limit).all()
