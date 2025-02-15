from pydantic import BaseModel

from deep_apply import apply


def my_func(value: str, **kwargs):
    key = kwargs.get("key")
    depth = kwargs.get("depth")

    if key == "id":
        return value

    if depth == "first_name" or depth == "child:first_name":
        return value

    return value.upper()


class Person(BaseModel):
    id: str
    first_name: str
    last_name: str


class Child(Person):
    pass


class Parent(Person):
    child: Child = Child(id="123abc", first_name="Jane", last_name="Doe")


parent = Parent(id="456def", first_name="John", last_name="Doe")


def test_ignore_key():
    data = parent
    data = apply(
        data=data,
        func=my_func,
    )

    assert data.id == "456def" and data.child.id == "123abc"


def test_ignore_key_depth():
    data = parent
    data = apply(
        data=data,
        func=my_func,
    )

    assert data.first_name == "John" and data.child.first_name == "Jane"
