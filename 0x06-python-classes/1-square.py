#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square with a private instance attribute size."""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size: The size of the square.
        """
        self.__size = size
