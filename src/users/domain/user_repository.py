from abc import ABC, abstractmethod
from src.users.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None: ...
