#!/usr/bin/python3
"""Defines the Rectangle class that inherits from Base.

This module provides a Rectangle class that inherits from the Base class.
The Rectangle class represents a rectangle shape and includes methods to
calculate its area, display it, update its attributes, and provide a dictionary
representation of a Rectangle instance.
"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle object that inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x offset of the rectangle in 2D space.
        y (int): The y offset of the rectangle in 2D space.
        id (int): The unique identifier of the rectangle, inherited from Base.

    Methods:
        area(): Calculates the area of the rectangle.
        display(): Prints the rectangle using the '#' character.
        __str__(): Returns a string representation of the rectangle.
        update(*args, **kwargs): Updates the rectangle's attributes.
        to_dictionary(): Returns a dictionary representation of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x offset of the rectangle. Defaults to 0.
            y (int, optional): The y offset of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it's an integer > 0."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it's an integer > 0."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: Gets or sets the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x offset of the rectangle,
        ensuring it's an integer >= 0."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Gets or sets the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y offset of the rectangle,
        ensuring it's an integer >= 0."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle instance using the '#' character,
        considering x and y offsets."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the Rectangle instance.

        Returns:
            str: A string representation of the rectangle.
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes
        with non-keyword or keyword arguments.

        Args:
            *args: A series of positional arguments.
            **kwargs: A series of keyword arguments.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle.

        Returns:
            dict: A dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
