from models.base import Base


class Rectangle(Base):
    """Represents a rectangle shape.

    Inherits from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The id of the rectangle
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be a positive integer")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be a positive integer")
        self._height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self._x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self._x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self._y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate of the rectangle.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
