from application.use_cases.base_use_case import BaseUseCase
from domain.models import User
from domain.schemas import UserCreate
from infrastructure.repositories.user_repository import user_repository
from sqlalchemy.orm import Session


class CreateUserUseCase(BaseUseCase[User]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.user_repository = user_repository

    def execute(self, user_in: UserCreate) -> User:
        return self.user_repository.create(self.db, obj_in=user_in.model_dump())
