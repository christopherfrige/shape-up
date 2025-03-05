from domain.models import Exercise
from domain.schemas import ExerciseCreate
from infrastructure.repositories.exercise_repository import ExerciseRepository
from sqlalchemy.orm import Session


class CreateExerciseUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ExerciseRepository(Exercise)

    def execute(self, exercise: ExerciseCreate) -> Exercise:
        return self.repository.create(self.db, obj_in=exercise)
