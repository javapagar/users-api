from src.users.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from src.users.domain.user import User


class TestInMemoryUserRepository:
    def test_save_in_memory_user_repository(self) -> None:
        user = User(name="Bill", age=43)
        user_repository = InMemoryUserRepository()

        assert len(user_repository._memory) == 0
        user_repository.save(user)
        assert len(user_repository._memory) == 1
