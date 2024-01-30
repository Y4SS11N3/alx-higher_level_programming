#!/usr/bin/python3
"""
This module defines the LockedClass.
The LockedClass restricts dynamic attribute creation to only 'first_name'.
"""


class LockedClass:
    """
    A class that allows only the creation of
    the 'first_name' instance attribute.
    Attempting to set any other attribute will raise an AttributeError.

    The restriction is implemented using the __slots__ mechanism.
    """

    __slots__ = ["first_name"]
