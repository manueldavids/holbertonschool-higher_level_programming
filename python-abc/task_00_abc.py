#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
