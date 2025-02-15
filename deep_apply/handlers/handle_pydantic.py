from typing import Callable

from pydantic import BaseModel

from deep_apply import utils


def handle_pydantic_model(apply: Callable, **kwargs) -> BaseModel:
    """
    Handle pydantic model.
    """

    data = kwargs["data"]
    depth: str | None = kwargs.get("depth")

    for key, value in iter(data):
        kwargs["key"] = key
        kwargs["data"] = value
        kwargs["depth"] = utils.set_current_depth(key=key, depth=depth)
        setattr(
            data,
            key,
            apply(
                **kwargs,
            ),
        )

    return data
