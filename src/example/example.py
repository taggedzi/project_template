#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Example(object):
    """
    This is an example Class to test with.
    """

    @property
    def double(self):
        """
        Take the initialized value an double it. Intentionally NO type checking.
        :param self:
        :return: x * 2
        """
        return self.x * 2

    def __init__(self, x=None):
        self.x = x


if __name__ == "__main__":
    e = Example(3)
    print(e.double)
