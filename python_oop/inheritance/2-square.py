#!/usr/bin/env python3
"""Complete square implementation."""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """A square with its own string representation."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

