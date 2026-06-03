#!/usr/bin/python3
"""
This module defines a Rectangle class with a customizable print_symbol.
"""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            rect_str += symbol * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Return a string representation to recreate the object."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement number_of_instances when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
