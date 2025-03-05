from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models.exercise import Exercise
from infrastructure.repositories.exercise_repository import ExerciseRepository
from sqlalchemy.orm import Session


class GetExerciseUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, exercise_id: int) -> Optional[Exercise]:
        return self.repository.get(self.db, id=exercise_id)
