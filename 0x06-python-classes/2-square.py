#!/usr/bin/python3

"""Must define a class Square."""


class Square:
    """Must represent a square."""

    def __init__(self, size=0):
        """Must initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
