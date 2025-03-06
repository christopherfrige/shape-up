from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import WorkoutPlan
from src.domain.schemas import WorkoutPlanCreate


class CreatePlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, workout_plan: WorkoutPlanCreate) -> WorkoutPlan:
        db_plan = WorkoutPlan(
            user_id=workout_plan.user_id,
            name=workout_plan.name,
            description=workout_plan.description,
            difficulty=workout_plan.difficulty,
            duration=workout_plan.duration,
            exercises=workout_plan.exercises,
        )
        self.session.add(db_plan)
        self.session.commit()
        self.session.refresh(db_plan)
        return db_plan
