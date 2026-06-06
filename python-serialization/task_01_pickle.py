#!/usr/bin/env python3
"""Module for pickling custom classes."""
import pickle


class CustomObject:
    """A custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from a file using pickle."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
