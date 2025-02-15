from typing import Callable


def handle_list(apply: Callable, **kwargs) -> list:
    """
    Handle list.
    """

    data = kwargs["data"]

    for index, value in enumerate(data):
        kwargs["data"] = value
        data[index] = apply(
            **kwargs,
        )

    return data
