#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance or inherited instance,
        otherwise False.
    """
    return isinstance(obj, a_class)
