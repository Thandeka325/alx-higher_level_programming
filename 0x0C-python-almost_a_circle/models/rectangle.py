#!/usr/bin/python3
"""Rectangle class module, inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class thet inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x position.
            y (int): y position.
            id (int): id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters and Setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    # Validation method
    def validate_integer(self, name, value, eq=True):
        """Validayes that the value is an integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    # Public method for the area
    def area(self):
        """Returns the area of the Rectangle instance.
        """
        return self.width * self.height

    # Public method to display the Rectangle
    def display(self):
        """Prints a string(#) representation of the rectangle instance.
        """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    # Overriding __str__method
    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    # Update method with *args and **kwargs
    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attr using */**args.
        """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle.
        """
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of this class.
        """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
