#!/usr/bin/env python3
"""Base geometry class."""


class BaseGeometry:
    """Define behavior shared by geometric figures."""

    def area(self):
        """Raise an exception because the base class has no area formula."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than zero."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
