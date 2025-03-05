from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseUseCase(ABC, Generic[T]):
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> T:
        """Execute the use case logic."""
        pass
