#!/usr/bin/python3
"""Rectangle implementation."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated width and height."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
