from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_session import WorkoutSession
from domain.schemas import WorkoutSessionUpdate
from sqlalchemy.orm import Session


class UpdateSessionUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(
        self, session_id: int, workout_session: WorkoutSessionUpdate
    ) -> WorkoutSession:
        db_session = (
            self.session.query(WorkoutSession)
            .filter(WorkoutSession.id == session_id)
            .first()
        )
        if not db_session:
            return None

        for key, value in workout_session.dict(exclude_unset=True).items():
            setattr(db_session, key, value)

        self.session.commit()
        self.session.refresh(db_session)
        return db_session
