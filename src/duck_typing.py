# src: https://realpython.com/duck-typing-python/

from math import pi
from typing import Protocol

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius

class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def perimeter(self) -> float:
        return 4 * self.side

class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

class Line:
    def __init__(self, length: float) -> None:
        self._length = length

    def length(self) -> float:
        return self._length


class Shape(Protocol):
    def area(self) -> float: ...
    
    def perimeter(self) -> float: ...

def describe_shape(shape: Shape):
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")


describe_shape(Circle(3))
describe_shape(Rectangle(12,5))
describe_shape(Square(12))
describe_shape(Line(25))

