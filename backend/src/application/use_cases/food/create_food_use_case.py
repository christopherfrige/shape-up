from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import Food
from src.domain.schemas import FoodCreate


class CreateFoodUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, food: FoodCreate) -> Food:
        db_food = Food(
            name=food.name,
            calories=food.calories,
            protein=food.protein,
            carbs=food.carbs,
            fat=food.fat,
            serving_size=food.serving_size,
            serving_unit=food.serving_unit,
            category=food.category,
            description=food.description,
        )
        self.session.add(db_food)
        self.session.commit()
        self.session.refresh(db_food)
        return db_food
