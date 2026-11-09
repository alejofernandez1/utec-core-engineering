#!/usr/bin/env python3
"""Rectangle implementation."""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated width and height."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
