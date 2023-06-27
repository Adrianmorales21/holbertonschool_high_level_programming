#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """objects and methods of the rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int, optional): x of the Rectangle. Defaults to 0.
            y (int, optional): y of the Rectangle. Defaults to 0.
            id (int, optional): id of the Rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Getter for the width attribute
            """
            return self.__width

        @width.setter
        def width(self, value):
            """setter for the width attribute"""
            self.__width = value

        @property
        def height(self):
            """getter for the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for the height attribute"""
            self.__height = value

        @property
        def x(self):
            """getter for the x attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            """setter for the x attribute """
            self.__x = value

        @property
        def y(self):
            """getter for the y attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter for the y attribute"""
            self.__y = value
