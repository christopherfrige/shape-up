from typing import List

from sqlalchemy.orm import Session

from src.domain.models import Exercise
from src.infrastructure.repositories.exercise_repository import ExerciseRepository


class ListExercisesUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, skip: int = 0, limit: int = 100) -> List[Exercise]:
        return self.repository.get_multi(self.db, skip=skip, limit=limit)
