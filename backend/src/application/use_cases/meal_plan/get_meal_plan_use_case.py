from application.use_cases.base_use_case import BaseUseCase
from domain.models.meal_plan import MealPlan
from sqlalchemy.orm import Session


class GetMealPlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, meal_plan_id: int) -> MealPlan:
        return self.session.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
