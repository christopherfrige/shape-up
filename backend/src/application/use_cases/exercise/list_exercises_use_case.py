from typing import List

from domain.models import Exercise
from infrastructure.repositories.exercise_repository import ExerciseRepository
from sqlalchemy.orm import Session


class ListExercisesUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, skip: int = 0, limit: int = 100) -> List[Exercise]:
        return self.repository.get_multi(self.db, skip=skip, limit=limit)
