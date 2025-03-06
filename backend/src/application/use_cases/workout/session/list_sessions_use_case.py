from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutSession


class ListSessionsUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[WorkoutSession]:
        return self.session.query(WorkoutSession).offset(skip).limit(limit).all()
