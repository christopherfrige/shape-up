from typing import Optional

from sqlalchemy.orm import Session

from src.application.services.calories import calculate_bmr
from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.user_use_case import GetUserUseCase


class CalculateBMRUseCase(BaseUseCase[Optional[float]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.get_user_use_case = GetUserUseCase(db)

    def execute(self, user_id: int) -> Optional[float]:
        user = self.get_user_use_case.execute(user_id)
        if not user:
            return None
        return calculate_bmr(user.weight, user.height, user.age, user.gender)
