from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Exercise
from src.domain.schemas import ExerciseUpdate


class UpdateExerciseUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, exercise_id: int, exercise: ExerciseUpdate) -> Exercise:
        db_exercise = self.session.query(Exercise).filter(Exercise.id == exercise_id).first()
        if not db_exercise:
            return None

        for key, value in exercise.dict(exclude_unset=True).items():
            setattr(db_exercise, key, value)

        self.session.commit()
        self.session.refresh(db_exercise)
        return db_exercise
