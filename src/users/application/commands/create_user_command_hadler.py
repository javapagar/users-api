from src.users.application.commands.create_user_command import CreateUserCommand
from src.users.domain.user_repository import UserRepository
from src.users.domain.user import User


class CreateUserCommandHandler:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, command: CreateUserCommand) -> None:
        user = User(command.name, command.age)

        self.user_repository.save(user)
