from sqlalchemy.orm import Session

from src.domain.models import Exercise
from src.domain.schemas import ExerciseCreate
from src.infrastructure.repositories.exercise_repository import ExerciseRepository


class CreateExerciseUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, exercise: ExerciseCreate) -> Exercise:
        return self.repository.create(self.db, obj_in=exercise)
