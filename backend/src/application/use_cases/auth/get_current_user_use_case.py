from typing import Optional

from application.use_cases.base_use_case import BaseUseCase
from application.use_cases.user.get_user_by_email_use_case import GetUserByEmailUseCase
from domain.models import User
from infrastructure.auth import decode_token
from sqlalchemy.orm import Session


class GetCurrentUserUseCase(BaseUseCase[Optional[User]]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.get_user_by_email_use_case = GetUserByEmailUseCase(db)

    def execute(self, token: str) -> Optional[User]:
        token_data = decode_token(token)
        if not token_data:
            return None
        return self.get_user_by_email_use_case.execute(token_data.email)
