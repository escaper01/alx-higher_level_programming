from tkinter import NO
from .base import Base
import sys

class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be > 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be > 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
    
    @x.setter
    def x(self, x):
        if isinstance(x, int):
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x
        else:
            raise TypeError("x must be an integer")
    
    @y.setter
    def y(self, y):
        if isinstance(y, int):
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
        else:
            raise TypeError("y must be an integer")
        
    
    def area(self):
        return self.width * self.height
    
    def display(self):
        for y in range(self.y):
                    sys.stdout.write("\n")
        
        for i in range(self.height):
            for x in range(self.x):
                    sys.stdout.write(" ")

            for j in range(self.width):
                sys.stdout.write("#")

            sys.stdout.write("\n")
            
    def __str__(self) -> str:
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id, 
                                                                self.x, self.y, 
                                                                self.width, self.height)
    
    def update(self, *args, **kwargs):
        if len(args) != 0:
            for i, elem in enumerate(args):
                if i == 0:
                    self.id = elem
                if i == 1:
                    self.width = elem
                if i == 2:
                    self.height = elem
                if i == 3:
                    self.x = elem
                if i == 4:
                    self.y = elem
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    