#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a subclass."""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of
    a class that inherited (directly or
    indirectly) from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
