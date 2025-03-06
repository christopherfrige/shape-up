from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.user.get_user_by_email_use_case import GetUserByEmailUseCase
from src.domain.models import User
from src.infrastructure.auth import verify_password


class AuthenticateUserUseCase(BaseUseCase[Optional[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.get_user_by_email_use_case = GetUserByEmailUseCase(db)

    def execute(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email_use_case.execute(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
