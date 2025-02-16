from deep_apply import constants


def add_key_to_depth(key: str, depth: str | None) -> str:
    """
    Add key to depth.

    :param key: The current key.
    :param depth: The current depth.
    """

    if depth:
        new_depth = f"{depth}:{key}"
    else:
        new_depth = key

    return new_depth


def can_handle(
    allowed_types: list[constants.SUPPORTED_TYPES],
    type_to_check: constants.SUPPORTED_TYPES,
) -> bool:
    """
    Check if type is allowed to be handled.
    An empty list means all types are allowed to be handled.

    :param allowed_types: A list of types allowed.
    :param type_to_check: Tye type to check.
    """

    if not allowed_types or (allowed_types and type_to_check in allowed_types):
        return True

    return False
