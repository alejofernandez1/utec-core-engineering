#!/usr/bin/env python3
"""Module defining a Square class with an area method."""


class Square:
    """Represent a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize the square and validate its size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
