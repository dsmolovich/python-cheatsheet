# https://fpy.li/11-2
# https://web.archive.org/web/20210505024221/https://julien.danjou.info/guide-python-static-class-abstract-methods/

# How methods work in Python
class Pizza:
    def __init__(self, size) -> None:
        self.size = size
    def get_size(self):
        return self.size

def _doctest_Pizza():
    """
    >>> Pizza.get_size  # doctest: +ELLIPSIS
    <function Pizza.get_size at 0x...>

    >>> Pizza.get_size()
    Traceback (most recent call last):
        ...
    TypeError: Pizza.get_size() missing 1 required positional argument: 'self'

    >>> Pizza.get_size(Pizza(42))
    42

    >>> Pizza(42).get_size  # doctest: +ELLIPSIS
    <bound method Pizza.get_size of <...Pizza object at 0x...>>

    >>> m = Pizza(42).get_size
    >>> m()
    42

    >>> m = Pizza(42).get_size
    >>> m.__self__  # doctest: +ELLIPSIS
    <...Pizza object at 0x...>

    >>> m == m.__self__.get_size
    True
    """


# Static methods
class StaticPizza:
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

def _doctest_StaticPizza():
    """
    >>> StaticPizza.mix_ingredients # doctest: +ELLIPSIS
    <function StaticPizza.mix_ingredients at 0x...>

    >>> StaticPizza().mix_ingredients # doctest: +ELLIPSIS
    <function StaticPizza.mix_ingredients at 0x...>

    >>> StaticPizza().cook == StaticPizza().cook
    False

    >>> StaticPizza().mix_ingredients is StaticPizza.mix_ingredients
    True

    >>> StaticPizza().mix_ingredients is StaticPizza().mix_ingredients
    True
    """


#Class methods
class ClassPizza():
    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius

def _doctest_ClassPizza():
    """
    >>> ClassPizza.get_radius  # doctest: +ELLIPSIS
    <bound method ClassPizza.get_radius of <class '...ClassPizza'>>

    >>> ClassPizza().get_radius  # doctest: +ELLIPSIS
    <bound method ClassPizza.get_radius of <class '...ClassPizza'>>

    >>> ClassPizza.get_radius == ClassPizza().get_radius
    True
    """

class PizzaWithClassMethodAsFactory:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())

class Fridge:
    def get_cheese(self):
        return 2
    def get_vegetables(self):
        return 3

def _doctest_PizzaWithClassMethodAsFactory():
    """
    >>> fridge = Fridge()
    >>> class_pizza = PizzaWithClassMethodAsFactory.from_fridge(fridge)

    >>> class_pizza  #doctest: +ELLIPSIS
    <...PizzaWithClassMethodAsFactory object at 0x...>

    >>> class_pizza.ingredients
    5
    """


# Abstract methods
from abc import ABC, abstractmethod
class AbstractPizza(ABC):
    @abstractmethod
    def get_radius(self):
        """Method that should do something."""

def _doctest_AbstractPizza():
    """
    >>> AbstractPizza()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class AbstractPizza with abstract method get_radius
    """
