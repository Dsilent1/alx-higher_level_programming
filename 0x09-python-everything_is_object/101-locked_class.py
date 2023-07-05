#!/usr/bin/python3
"""Must efine a locked class."""


class LockedClass:
    """
    Should prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
