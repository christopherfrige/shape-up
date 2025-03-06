from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Progress
from src.domain.schemas import ProgressCreate


class CreateProgressUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, progress: ProgressCreate) -> Progress:
        db_progress = Progress(
            user_id=progress.user_id,
            date=progress.date,
            weight=progress.weight,
            body_fat=progress.body_fat,
            muscle_mass=progress.muscle_mass,
            notes=progress.notes,
        )
        self.session.add(db_progress)
        self.session.commit()
        self.session.refresh(db_progress)
        return db_progress
