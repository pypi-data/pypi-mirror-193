from collections.abc import Mapping
from functools import reduce


def deep_get(dictionary: dict, *keys, default=None):
    """Safely return the value of an arbitrarily nested map
    Inspired by https://bit.ly/3a0hq9E
    """
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, Mapping) else default, keys, dictionary)
