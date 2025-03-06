from typing import List

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Progress
from src.infrastructure.repositories.progress_repository import progress_repository


class GetUserProgressUseCase(BaseUseCase[List[Progress]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.progress_repository = progress_repository

    def execute(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Progress]:
        return self.progress_repository.get_by_user(
            self.db, user_id=user_id, skip=skip, limit=limit
        )
