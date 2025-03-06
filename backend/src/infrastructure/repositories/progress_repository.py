from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.domain.models import Progress
from src.infrastructure.repositories.base_repository import BaseRepository


class ProgressRepository(BaseRepository[Progress]):
    def get_by_user(
        self, db: Session, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Progress]:
        return (
            db.query(Progress)
            .filter(Progress.user_id == user_id)
            .order_by(desc(Progress.date))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_latest(self, db: Session, user_id: int) -> Optional[Progress]:
        return (
            db.query(Progress)
            .filter(Progress.user_id == user_id)
            .order_by(desc(Progress.date))
            .first()
        )

    def get_by_date_range(
        self, db: Session, user_id: int, start_date: datetime, end_date: datetime
    ) -> List[Progress]:
        return (
            db.query(Progress)
            .filter(
                Progress.user_id == user_id,
                Progress.date >= start_date,
                Progress.date <= end_date,
            )
            .order_by(desc(Progress.date))
            .all()
        )


progress_repository = ProgressRepository(Progress)
