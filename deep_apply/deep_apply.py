import copy
from typing import Callable, TypeVar

from deep_apply import utils
from deep_apply.handlers.handle_dict import handle_dict
from deep_apply.handlers.handle_list import handle_list
from deep_apply.handlers.handle_pydantic import handle_pydantic_model
from deep_apply.handlers.handle_set import handle_set
from deep_apply.handlers.handle_tuple import handle_tuple

T = TypeVar("T")


def __apply(
    **kwargs,
) -> T:
    """
    Apply.
    """

    data = kwargs["data"]
    apply_func: Callable = kwargs["apply_func"]
    key: str | None = kwargs.get("key")
    depth: str | None = kwargs.get("depth")

    if utils.is_list(data):
        return handle_list(__apply, **kwargs)

    elif utils.is_set(data):
        return handle_set(__apply, **kwargs)

    elif utils.is_tuple(data):
        return handle_tuple(__apply, **kwargs)

    elif utils.is_dict(data):
        return handle_dict(__apply, **kwargs)

    elif utils.is_pydantic_model(data):
        return handle_pydantic_model(__apply, **kwargs)

    else:
        return apply_func(data, **{"key": key, "depth": depth})


def apply(
    data: T,
    func: Callable,
) -> T:
    """
    Deep traverse through an object and apply a function on its values.

    Supports the following objects:
     * Dictionaries
     * Lists
     * Sets
     * Tuples
     * Pydantic models

    :param data: The data.
    :param func: Function to apply on values.
    """

    return __apply(
        data=copy.deepcopy(data),
        apply_func=func,
    )
