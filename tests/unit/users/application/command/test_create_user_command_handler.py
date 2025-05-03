from expects import expect
from doublex_expects import have_been_called_with
from doublex import Mimic, Spy

from src.users.application.commands.create_user_command_hadler import (
    CreateUserCommandHandler,
)
from src.users.domain.user import User
from src.users.application.commands.create_user_command import CreateUserCommand
from src.users.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


class TestCreateUserCommandHandler:
    def test_create_user_command_handler(self) -> None:
        name: str = "Bill"
        age: int = 42

        command = CreateUserCommand(name=name, age=age)

        user_repository = Mimic(Spy, InMemoryUserRepository)
        handler = CreateUserCommandHandler(user_repository)

        user = User(name=name, age=age)

        handler.execute(command)

        expect(user_repository.save).to(have_been_called_with(user))
