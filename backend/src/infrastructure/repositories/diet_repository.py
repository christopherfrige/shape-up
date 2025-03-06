from typing import List

from sqlalchemy.orm import Session

from src.domain.models import Diet, DietFood, MealFood, MealPlan
from src.infrastructure.repositories.base_repository import BaseRepository


class DietRepository(BaseRepository[Diet]):
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Diet]:
        return db.query(Diet).filter(Diet.user_id == user_id).offset(skip).limit(limit).all()

    def add_food(self, db: Session, *, diet_id: int, food_id: int, quantity: float) -> DietFood:
        db_obj = DietFood(diet_id=diet_id, food_id=food_id, quantity=quantity)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove_food(self, db: Session, *, diet_id: int, food_id: int) -> bool:
        db_obj = (
            db.query(DietFood)
            .filter(DietFood.diet_id == diet_id, DietFood.food_id == food_id)
            .first()
        )
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False

    def get_foods(self, db: Session, *, diet_id: int) -> List[DietFood]:
        return db.query(DietFood).filter(DietFood.diet_id == diet_id).all()

    def create_meal_plan(
        self, db: Session, *, diet_id: int, day_of_week: int, meal_type: str
    ) -> MealPlan:
        db_obj = MealPlan(diet_id=diet_id, day_of_week=day_of_week, meal_type=meal_type)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_food_to_meal(
        self, db: Session, *, meal_plan_id: int, food_id: int, quantity: float
    ) -> MealFood:
        db_obj = MealFood(meal_plan_id=meal_plan_id, food_id=food_id, quantity=quantity)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_meal_plans(self, db: Session, *, diet_id: int) -> List[MealPlan]:
        return db.query(MealPlan).filter(MealPlan.diet_id == diet_id).all()

    def get_meal_foods(self, db: Session, *, meal_plan_id: int) -> List[MealFood]:
        return db.query(MealFood).filter(MealFood.meal_plan_id == meal_plan_id).all()


diet_repository = DietRepository(Diet)
