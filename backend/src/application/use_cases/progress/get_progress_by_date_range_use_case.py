from datetime import datetime
from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models import Progress
from infrastructure.repositories.progress_repository import progress_repository
from sqlalchemy.orm import Session


class GetProgressByDateRangeUseCase(BaseUseCase[List[Progress]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.progress_repository = progress_repository

    def execute(
        self, user_id: int, start_date: datetime, end_date: datetime
    ) -> List[Progress]:
        return self.progress_repository.get_by_date_range(
            self.db, user_id=user_id, start_date=start_date, end_date=end_date
        )
