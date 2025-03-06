from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutSession
from src.domain.schemas import WorkoutSessionCreate


class CreateSessionUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, workout_session: WorkoutSessionCreate) -> WorkoutSession:
        db_session = WorkoutSession(
            user_id=workout_session.user_id,
            workout_plan_id=workout_session.workout_plan_id,
            date=workout_session.date,
            duration=workout_session.duration,
            notes=workout_session.notes,
        )
        self.session.add(db_session)
        self.session.commit()
        self.session.refresh(db_session)
        return db_session
