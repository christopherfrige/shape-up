from typing import List, Optional

from domain.models import Exercise, ExerciseCategory
from infrastructure.repositories.base_repository import BaseRepository
from sqlalchemy import or_
from sqlalchemy.orm import Session


class ExerciseRepository(BaseRepository[Exercise]):
    def get_by_name(self, db: Session, name: str) -> Optional[Exercise]:
        return db.query(Exercise).filter(Exercise.name == name).first()

    def get_by_category(
        self, db: Session, category: ExerciseCategory, skip: int = 0, limit: int = 100
    ) -> List[Exercise]:
        return (
            db.query(Exercise)
            .filter(Exercise.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search_by_name(
        self, db: Session, name: str, skip: int = 0, limit: int = 100
    ) -> List[Exercise]:
        return (
            db.query(Exercise)
            .filter(Exercise.name.ilike(f"%{name}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search_by_muscle_group(
        self, db: Session, muscle_group: str, skip: int = 0, limit: int = 100
    ) -> List[Exercise]:
        return (
            db.query(Exercise)
            .filter(Exercise.muscle_groups.ilike(f"%{muscle_group}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_difficulty(
        self, db: Session, difficulty_level: int, skip: int = 0, limit: int = 100
    ) -> List[Exercise]:
        return (
            db.query(Exercise)
            .filter(Exercise.difficulty_level == difficulty_level)
            .offset(skip)
            .limit(limit)
            .all()
        )


exercise_repository = ExerciseRepository(Exercise)
