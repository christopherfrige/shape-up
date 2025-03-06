from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.infrastructure.repositories.progress_repository import progress_repository


class CalculateWeightChangeUseCase(BaseUseCase[Optional[float]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.progress_repository = progress_repository

    def execute(self, user_id: int, days: int = 30) -> Optional[float]:
        latest = self.progress_repository.get_latest(self.db, user_id=user_id)
        if not latest:
            return None

        start_date = datetime.utcnow() - datetime.timedelta(days=days)
        old_progress = self.progress_repository.get_by_date_range(
            self.db, user_id=user_id, start_date=start_date, end_date=latest.date
        )

        if not old_progress:
            return None

        return latest.weight - old_progress[0].weight
