#!/usr/bin/env python3
"""Complete rectangle implementation."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with area and readable representation."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
