#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """A Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of Student."""
        return self.__dict__
