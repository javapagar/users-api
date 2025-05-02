from dataclasses import dataclass


@dataclass
class CreateUserCommand:
    name: str
    age: int
