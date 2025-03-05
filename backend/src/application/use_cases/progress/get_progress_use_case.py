from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models.progress import Progress
from sqlalchemy.orm import Session


class GetProgressUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, progress_id: int) -> Progress:
        return self.session.query(Progress).filter(Progress.id == progress_id).first()
