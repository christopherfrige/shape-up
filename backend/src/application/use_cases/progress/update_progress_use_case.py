from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from domain.models.progress import Progress
from domain.schemas import ProgressUpdate
from sqlalchemy.orm import Session


class UpdateProgressUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, progress_id: int, progress: ProgressUpdate) -> Progress:
        db_progress = (
            self.session.query(Progress).filter(Progress.id == progress_id).first()
        )
        if not db_progress:
            return None

        for key, value in progress.dict(exclude_unset=True).items():
            setattr(db_progress, key, value)

        self.session.commit()
        self.session.refresh(db_progress)
        return db_progress
