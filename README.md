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

```python
import deep_apply


# 1. Create your function.
#    This function will call upper() on strings.
#
#    Note: If your function will only extract data, simply return the value 
#    back as it is when done.
def to_upper(value, **kwargs):
    """
    To upper case.
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

    # To upper
    if not ignore and isinstance(value, str):
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

# 3. Apply function on the data.
data = deep_apply.apply(data=data, func=to_upper)
```

### Result

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
