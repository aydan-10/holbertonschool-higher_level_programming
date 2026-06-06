#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """A Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of Student."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student from a dictionary."""
        for k, v in json.items():
            setattr(self, k, v)
