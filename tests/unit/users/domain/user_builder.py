from faker import Faker
from random import randint
from src.users.domain.user import User


class UserBuilder:
    def __init__(self) -> None:
        self.__initialize()

    def __initialize(self) -> None:
        fake = Faker()
        self._name = fake.name()
        self._age = randint(18, 100)

    def with_name(self, name: str) -> "UserBuilder":
        self._name = name
        return self

    def with_age(self, age: int) -> "UserBuilder":
        self._age = age
        return self

    def build(self) -> User:
        return User(name=self._name, age=self._age)
