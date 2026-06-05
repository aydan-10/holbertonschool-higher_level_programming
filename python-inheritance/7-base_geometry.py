#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A class with public instance methods area and integer_validator."""

    def area(self):
        """Raises an Exception as it is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
