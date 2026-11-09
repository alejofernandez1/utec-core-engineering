#!/usr/bin/python3
"""Square implementation."""

Rectangle = __import__("1-rectangle").Rectangle


class Square(Rectangle):
    """A square represented as a specialized rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
