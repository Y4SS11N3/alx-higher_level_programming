#!/usr/bin/python3
"""Defines a function to check object's
instance with inheritance consideration."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of,
    or if the object is an instance of
    a class that inherited from, the specified class."""
    return isinstance(obj, a_class)
