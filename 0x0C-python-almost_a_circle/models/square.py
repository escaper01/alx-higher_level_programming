#!/usr/bin/python3
from .rectangle import Rectangle

class Square(Rectangle):
    """_summary_
        Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width


    @size.setter
    def size(self, val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    
    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }


    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "[Square] ({0}) {1}/{2} - {3}".format(self.id,
                                                     self.x, self.y,
                                                     self.width)