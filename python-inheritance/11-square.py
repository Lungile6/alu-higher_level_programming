#!/usr/bin/python3
"""Define a Rectangle subclass Square."""
Rectanbgle = __import__('9-Rectangle').Rectangle


class square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initalize a new square.
        Args:
          size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
