from fastapi import APIRouter, Depends
from http.client import CREATED

from src.delivery.api.v1.users.users_request import UserRequest
from src.users.application.commands.create_user_command import CreateUserCommand
from src.users.application.commands.create_user_command_hadler import (
    CreateUserCommandHandler,
)

users_router = APIRouter()


def _get_create_users_command_handler() -> CreateUserCommandHandler:
    return CreateUserCommandHandler()


@users_router.post("/", status_code=CREATED)
def create_user(
    user_request: UserRequest,
    handler: CreateUserCommandHandler = Depends(_get_create_users_command_handler),
) -> None:
    command = CreateUserCommand(**dict(user_request))
    handler.execute(command)
