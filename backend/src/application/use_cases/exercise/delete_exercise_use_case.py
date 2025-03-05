from application.use_cases.base_use_case import BaseUseCase
from domain.models.exercise import Exercise
from sqlalchemy.orm import Session


class DeleteExerciseUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, exercise_id: int) -> bool:
        db_exercise = (
            self.session.query(Exercise).filter(Exercise.id == exercise_id).first()
        )
        if not db_exercise:
            return False

        self.session.delete(db_exercise)
        self.session.commit()
        return True
