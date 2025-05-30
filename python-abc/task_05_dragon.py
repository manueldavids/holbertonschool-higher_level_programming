#!/usr/bin/python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin that adds swimming ability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying abilities."""
    def roar(self):
        print("The dragon roars!")
