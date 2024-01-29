#!/usr/bin/python3
"""
Module 9-rectangle
Defines Rectangle class with class methods square and bigger_or_equal.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rows = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Representation for recreation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message on deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return bigger rectangle based on area."""
        if not isinstance(rect_1, Rectangle) or \
                not isinstance(rect_2, Rectangle):
            rect = 'rect_1' if not isinstance(rect_1, Rectangle) else 'rect_2'
            raise TypeError(f"{rect} must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return new Rectangle instance with equal width and height."""
        return cls(size, size)
