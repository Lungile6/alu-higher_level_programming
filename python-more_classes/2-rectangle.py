#!/usr/bin/python3
"""Define the Rectangle."""


class Rectangle:
    """Represents a class rectangle."""

    def __init__(self, width=0, height=0):
        """Intialize the new rectanlge.
        Args:
          width(int): The width must be an integer.
          height(int): The height must be an integer.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
