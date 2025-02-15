from typing import Callable


def handle_tuple(apply: Callable, **kwargs) -> tuple:
    """
    Handle tuple.
    """

    data = kwargs["data"]
    data = list(data)

    for index, value in enumerate(data):
        kwargs["data"] = value
        data[index] = apply(
            **kwargs,
        )

    data = tuple(data)

    return data
