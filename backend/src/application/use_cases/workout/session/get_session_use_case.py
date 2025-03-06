from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutSession


class GetSessionUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, session_id: int) -> WorkoutSession:
        return self.session.query(WorkoutSession).filter(WorkoutSession.id == session_id).first()
