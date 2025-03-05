from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_session import WorkoutSession
from sqlalchemy.orm import Session


class GetSessionUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, session_id: int) -> WorkoutSession:
        return (
            self.session.query(WorkoutSession)
            .filter(WorkoutSession.id == session_id)
            .first()
        )
