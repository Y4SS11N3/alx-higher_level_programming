#!/usr/bin/python3
"""Defines the Square class with size property and area, print methods."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
