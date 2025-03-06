from typing import Optional

from sqlalchemy.orm import Session

from src.application.services.calories import calculate_calorie_goal
from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.calories.calculate_tdee_use_case import CalculateTDEEUseCase


class CalculateCalorieGoalUseCase(BaseUseCase[Optional[float]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.calculate_tdee_use_case = CalculateTDEEUseCase(db)

    def execute(self, user_id: int, goal: str) -> Optional[float]:
        tdee = self.calculate_tdee_use_case.execute(user_id)
        if not tdee:
            return None
        return calculate_calorie_goal(tdee, goal)
