from typing import Optional

from sqlalchemy.orm import Session

from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.user.get_user_by_email_use_case import GetUserByEmailUseCase
from src.domain.models import User
from src.infrastructure.auth import decode_token


class GetCurrentUserUseCase(BaseUseCase[Optional[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.get_user_by_email_use_case = GetUserByEmailUseCase(db)

    def execute(self, token: str) -> Optional[User]:
        token_data = decode_token(token)
        if not token_data:
            return None
        return self.get_user_by_email_use_case.execute(token_data.email)
