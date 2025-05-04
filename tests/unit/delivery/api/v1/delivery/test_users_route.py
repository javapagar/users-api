from http.client import CREATED
from fastapi.testclient import TestClient
from expects import expect, equal
from doublex import Spy, Mimic
from doublex_expects import have_been_called_with

from main import app
from src.users.application.commands.create_user_command import CreateUserCommand
from src.users.application.commands.create_user_command_hadler import (
    CreateUserCommandHandler,
)
from src.delivery.api.v1.users.users_router import _get_create_users_command_handler
from src.delivery.api.v1.users.users_request import UserRequest


class TestUsersRouter:
    def test_create_user(self) -> None:
        name: str = "Bill"
        age: int = 42
        payload = {"name": name, "age": age}
        user_request = UserRequest(name=name, age=age)
        command = CreateUserCommand(user_request.name, user_request.age)
        client = TestClient(app)

        handler = Mimic(Spy, CreateUserCommandHandler)
        app.dependency_overrides[_get_create_users_command_handler] = lambda: handler
        response = client.post("/api/v1/users", json=payload)

        expect(response.status_code).to(equal(CREATED))
        expect(handler.execute).to(have_been_called_with(command))
