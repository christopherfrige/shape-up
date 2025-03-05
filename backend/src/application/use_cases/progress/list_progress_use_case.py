from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models.progress import Progress
from sqlalchemy.orm import Session


class ListProgressUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[Progress]:
        return self.session.query(Progress).offset(skip).limit(limit).all()
