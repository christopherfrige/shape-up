from typing import List

from application.use_cases.base_use_case import BaseUseCase
from domain.models.food import Food
from sqlalchemy.orm import Session


class ListFoodsUseCase(BaseUseCase):
    def __init__(self, session: Session):
        super().__init__(session)

    def execute(self, skip: int = 0, limit: int = 100) -> List[Food]:
        return self.session.query(Food).offset(skip).limit(limit).all()
