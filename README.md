# Deep Apply

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/deep-apply?color=blue)](https://pypi.python.org/pypi/deep-apply)
[![PyPI](https://img.shields.io/pypi/v/deep-apply?color=blue)](https://pypi.python.org/pypi/deep-apply)
[![PyPI - License](https://img.shields.io/pypi/l/deep-apply)](https://pypi.python.org/pypi/deep-apply)

[![tests](https://github.com/zaironjacobs/deep-apply/actions/workflows/test.yml/badge.svg)](https://github.com/zaironjacobs/deep-apply/actions/workflows/test.yml)

Deep traverse through an object and apply a function on its values.

Supports the following objects:

* Dictionaries
* Lists
* Sets
* Tuples
* Pydantic models

### Install

```bash
pip install deep-apply
```

### Usage

#### Apply upper() on values

```python
import deep_apply


# 1. Create your callback function. Will call upper() on strings.
def to_upper(value, **kwargs):
    """
    To uppercase.
    """

    # Apply upper() and return the value
    if isinstance(value, str):
        return value.upper()

    return value


# 2. Your data.
data = [
    {
        "id": "pZnZMffPCpJx",
        "name": "John Doe",
        "hobbies": {
            "id": "OlVZysGsIywW",
            "sport": ["football", "tennis"],
            "music": ["singing", "guitar", "piano"],
            "random_numbers": [4, 10, 25],
        },
    }
]

# 3. Run apply()
data = deep_apply.apply(data=data, func=to_upper)
```

#### Result

```json
[
  {
    "id": "pZnZMffPCpJx",
    "name": "JOHN DOE",
    "hobbies": {
      "id": "OlVZysGsIywW",
      "sport": [
        "FOOTBALL",
        "TENNIS"
      ],
      "music": [
        "singing",
        "guitar",
        "piano"
      ]
    }
  }
]
```

### Ignore keys

You can get the current `key` or the current `depth` from `**kwargs` and add a condition e.g. to skip a specific key
everywhere.

```python
def to_upper(value, **kwargs):
    """
    To uppercase.
    """

    key = kwargs.get("key")
    depth = kwargs.get("depth")

    ignore = False

    # Ignore the key/field id everywhere (dictionaries or pydantic models)
    if key == "id":
        ignore = True

    # Ignore the list of music found under hobbies
    elif depth == "hobbies:music":
        ignore = True

    # Apply upper() and return the value
    if not ignore and isinstance(value, str):
        return value.upper()

    return value
```