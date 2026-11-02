#!/usr/bin/env python3
"""Module defining a Square class with position and string representation."""


class Square:
    """Represent a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating its type and value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validating its values."""
        if (type(value) is not tuple or len(value) != 2
                or not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # and its position."""
        print(self.__str__())

    def __str__(self):
        """Return the square as a string."""
        if self.__size == 0:
            return ""

        rows = [" " * self.__position[0] + "#" * self.__size
                for _ in range(self.__size)]

        return "\n" * self.__position[1] + "\n".join(rows)
