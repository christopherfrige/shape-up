from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import MealPlan
from src.domain.schemas import MealPlanUpdate


class UpdateMealPlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, meal_plan_id: int, meal_plan: MealPlanUpdate) -> MealPlan:
        db_meal_plan = self.session.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
        if not db_meal_plan:
            return None

        for key, value in meal_plan.dict(exclude_unset=True).items():
            setattr(db_meal_plan, key, value)

        self.session.commit()
        self.session.refresh(db_meal_plan)
        return db_meal_plan
