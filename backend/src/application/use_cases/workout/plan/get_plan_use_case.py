from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_plan import WorkoutPlan
from sqlalchemy.orm import Session


class GetPlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, plan_id: int) -> WorkoutPlan:
        return self.session.query(WorkoutPlan).filter(WorkoutPlan.id == plan_id).first()
