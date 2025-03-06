from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutSession


class DeleteSessionUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, session_id: int) -> bool:
        db_session = (
            self.session.query(WorkoutSession).filter(WorkoutSession.id == session_id).first()
        )
        if not db_session:
            return False

        self.session.delete(db_session)
        self.session.commit()
        return True
