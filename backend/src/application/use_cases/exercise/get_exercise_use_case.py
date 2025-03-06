from typing import Optional

from sqlalchemy.orm import Session

from src.domain.models import Exercise
from src.infrastructure.repositories.exercise_repository import ExerciseRepository


class GetExerciseUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, exercise_id: int) -> Optional[Exercise]:
        return self.repository.get(self.db, id=exercise_id)
