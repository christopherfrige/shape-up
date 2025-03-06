from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Progress


class GetProgressUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, progress_id: int) -> Progress:
        return self.session.query(Progress).filter(Progress.id == progress_id).first()
