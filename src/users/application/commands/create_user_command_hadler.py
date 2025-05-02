from src.users.application.commands.create_user_command import CreateUserCommand


class CreateUserCommandHandler:
    def execute(self, command: CreateUserCommand) -> None: ...
