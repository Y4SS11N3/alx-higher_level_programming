#!/usr/bin/python3
"""Defines the Square class with size and position attributes."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character."""
        print(self.__str__())

    def __str__(self):
        """Defines the print() representation of the square."""
        if self.__size == 0:
            return ""
        else:
            rows = []
            if self.__position[1] > 0:
                rows.append("\n" * (self.__position[1] - 1))
            for _ in range(self.__size):
                rows.append(" " * self.__position[0] + "#" * self.__size)
            return "\n".join(rows)
