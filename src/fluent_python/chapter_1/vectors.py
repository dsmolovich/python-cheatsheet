from math import hypot

class Vector:
    """
    >>> v1 = Vector(2, 3)
    >>> v1
    Vector(2, 3)

    >>> v2 = Vector(7, -5)
    >>> v1 + v2
    Vector(9, -2)

    >>> v = Vector(3, 4)
    >>> v * 3
    Vector(9, 12)

    >>> abs(v)
    5.0
    """
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
    
    def __add__(self, other_vector: 'Vector'):
        new_vector = Vector(x=self.x + other_vector.x,
                            y=self.y + other_vector.y)
        return new_vector

    def __mul__(self, scalar: float):
        new_vector = Vector(x=self.x * scalar,
                            y= self.y * scalar)
        return new_vector

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __abs__(self) -> float:
        return hypot(self.x, self.y)
