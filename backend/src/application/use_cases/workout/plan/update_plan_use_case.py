from application.use_cases.base_use_case import BaseUseCase
from domain.models.workout_plan import WorkoutPlan
from domain.schemas import WorkoutPlanUpdate
from sqlalchemy.orm import Session


class UpdatePlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, plan_id: int, workout_plan: WorkoutPlanUpdate) -> WorkoutPlan:
        db_plan = (
            self.session.query(WorkoutPlan).filter(WorkoutPlan.id == plan_id).first()
        )
        if not db_plan:
            return None

        for key, value in workout_plan.dict(exclude_unset=True).items():
            setattr(db_plan, key, value)

        self.session.commit()
        self.session.refresh(db_plan)
        return db_plan
