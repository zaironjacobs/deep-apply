from typing import Callable

from deep_apply import helpers


def handle_dict(apply: Callable, **kwargs) -> dict:
    """
    Handle dict.
    """

    data = kwargs["data"]
    depth: str | None = kwargs.get("depth")

    for key, value in data.items():
        kwargs["key"] = key
        kwargs["data"] = value
        kwargs["depth"] = helpers.add_key_to_depth(key=key, depth=depth)
        data[key] = apply(
            **kwargs,
        )

    return data
