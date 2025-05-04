from tests.unit.users.domain.user_builder import UserBuilder


def test_create_user() -> None:
    name = "Bill"
    age = 42

    user = UserBuilder().with_name(name).with_age(age).build()

    assert user.name == name
    assert user.age == age
