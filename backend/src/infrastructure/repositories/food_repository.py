from typing import List, Optional

from domain.models import Food, FoodCategory
from infrastructure.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session


class FoodRepository(BaseRepository[Food]):
    def get_by_category(
        self, db: Session, *, category: FoodCategory, skip: int = 0, limit: int = 100
    ) -> List[Food]:
        return (
            db.query(Food)
            .filter(Food.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_name(self, db: Session, *, name: str) -> Optional[Food]:
        return db.query(Food).filter(Food.name == name).first()

    def search_by_name(
        self, db: Session, *, name: str, skip: int = 0, limit: int = 100
    ) -> List[Food]:
        return (
            db.query(Food)
            .filter(Food.name.ilike(f"%{name}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )


food_repository = FoodRepository(Food)
