import copy
from typing import Callable, TypeVar

from typing_extensions import get_args

from deep_apply import utils, helpers
from deep_apply.exceptions import DeepApplyException
from deep_apply.handlers.handle_dict import handle_dict
from deep_apply.handlers.handle_list import handle_list
from deep_apply.handlers.handle_pydantic import handle_pydantic_model
from deep_apply.handlers.handle_set import handle_set
from deep_apply.handlers.handle_tuple import handle_tuple
from deep_apply import constants


T = TypeVar("T")


def __apply(
    **kwargs,
) -> T:
    """
    Apply.
    """

    data = kwargs["data"]
    apply_func: Callable = kwargs["apply_func"]
    allowed_types: list[constants.SUPPORTED_TYPES] = kwargs["allowed_types"]
    key: str = kwargs["key"]
    depth_key: str = kwargs["depth_key"]
    depth_level: int = kwargs["depth_level"]

    if utils.is_list(data):
        if helpers.can_handle(
            allowed_types=allowed_types, type_to_check=type(data).__name__
        ):
            return handle_list(__apply, **kwargs)

        return data

    elif utils.is_set(data):
        if helpers.can_handle(
            allowed_types=allowed_types, type_to_check=type(data).__name__
        ):
            return handle_set(__apply, **kwargs)

        return data

    elif utils.is_tuple(data):
        if helpers.can_handle(
            allowed_types=allowed_types, type_to_check=type(data).__name__
        ):
            return handle_tuple(__apply, **kwargs)

        return data

    elif utils.is_dict(data):
        if helpers.can_handle(
            allowed_types=allowed_types, type_to_check=type(data).__name__
        ):
            return handle_dict(__apply, **kwargs)

        return data

    elif utils.is_pydantic_model(data):
        if helpers.can_handle(allowed_types=allowed_types, type_to_check="pydantic"):
            return handle_pydantic_model(__apply, **kwargs)

        return data

    else:
        return apply_func(
            **{
                "value": data,
                "key": key,
                "depth_key": depth_key,
                "depth_level": depth_level,
            }
        )


def apply(
    data: T,
    func: Callable,
    allowed_types: list[constants.SUPPORTED_TYPES] = None,
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
    :param func: Function to apply on data values.
    :param allowed_types: Optional - Only traverse through these object types.
    """

    if allowed_types is None:
        allowed_types = []

    if allowed_types:
        supported_types_set = set(get_args(constants.SUPPORTED_TYPES))
        for _type in allowed_types:
            if _type not in supported_types_set:
                raise DeepApplyException(
                    f"Invalid type received in allowed_types: {_type}"
                )

    return __apply(
        data=copy.deepcopy(data),
        apply_func=func,
        allowed_types=allowed_types,
        key="",
        depth_key="",
        depth_level=0,
    )
