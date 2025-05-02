from typing import List

from src.users.domain.user_repository import UserRepository
from src.users.domain.user import User


class InMemoryUserRepository(UserRepository):
    _memory: List[User] = []

    def save(self, user: User) -> None:
        self._memory.append(user)
