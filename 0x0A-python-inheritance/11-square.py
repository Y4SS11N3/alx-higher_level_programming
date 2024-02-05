#!/usr/bin/python3
"""Enhances the Square class with proper
initialization and area calculation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from Rectangle."""
    def __init__(self, size):
        """Initializes the square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
