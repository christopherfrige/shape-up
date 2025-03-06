from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import MealPlan


class DeleteMealPlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, meal_plan_id: int) -> bool:
        db_meal_plan = self.session.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
        if not db_meal_plan:
            return False

        self.session.delete(db_meal_plan)
        self.session.commit()
        return True
