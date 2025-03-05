from application.use_cases.base_use_case import BaseUseCase
from domain.models.meal_plan import MealPlan
from domain.schemas import MealPlanCreate
from sqlalchemy.orm import Session


class CreateMealPlanUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, meal_plan: MealPlanCreate) -> MealPlan:
        db_meal_plan = MealPlan(
            user_id=meal_plan.user_id,
            name=meal_plan.name,
            description=meal_plan.description,
            total_calories=meal_plan.total_calories,
            meals=meal_plan.meals,
        )
        self.session.add(db_meal_plan)
        self.session.commit()
        self.session.refresh(db_meal_plan)
        return db_meal_plan
