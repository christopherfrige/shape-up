from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.models import User
from src.domain.schemas import UserCreate
from src.infrastructure.repositories.user_repository import user_repository


class CreateUserUseCase(BaseUseCase[User]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.user_repository = user_repository

    def execute(self, user_in: UserCreate) -> User:
        return self.user_repository.create(self.db, obj_in=user_in.model_dump())
