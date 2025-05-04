from src.users.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from tests.unit.users.domain.user_builder import UserBuilder


class TestInMemoryUserRepository:
    def test_save_in_memory_user_repository(self) -> None:
        user = UserBuilder().build()
        user_repository = InMemoryUserRepository()

        assert len(user_repository._memory) == 0
        user_repository.save(user)
        assert len(user_repository._memory) == 1
