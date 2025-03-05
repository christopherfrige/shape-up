from typing import Optional

from application.services.calories import calculate_tdee
from application.use_cases.base_use_case import BaseUseCase
from application.use_cases.calories.calculate_bmr_use_case import CalculateBMRUseCase
from application.use_cases.user_use_case import GetUserUseCase
from domain.models import ActivityLevel
from sqlalchemy.orm import Session


class CalculateTDEEUseCase(BaseUseCase[Optional[float]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.get_user_use_case = GetUserUseCase(db)
        self.calculate_bmr_use_case = CalculateBMRUseCase(db)

    def execute(self, user_id: int) -> Optional[float]:
        user = self.get_user_use_case.execute(user_id)
        if not user:
            return None

        bmr = self.calculate_bmr_use_case.execute(user_id)
        if not bmr:
            return None

        return calculate_tdee(bmr, user.activity_level)
