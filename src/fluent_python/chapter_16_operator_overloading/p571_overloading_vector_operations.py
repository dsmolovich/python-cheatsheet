from src.fluent_python.chapter_12_special_methods_for_sequences.p421_multidemntial_vector_formatting import Vector
import itertools

class VectorOverload(Vector):
    """
    >>> v1 = VectorOverload([1, 2, 3])
    >>> v2 = VectorOverload([4, 5])
    >>> v1 + v2
    Vector([5.0, 7.0, 3.0])

    >>> v1 + [4, 5]
    Vector([5.0, 7.0, 3.0])

    >>> [4, 5] + v1
    Vector([5.0, 7.0, 3.0])

    >>> (4, 5) + v1
    Vector([5.0, 7.0, 3.0])

    >>> v1 + 'ABC'
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'VectorOverload' and 'str'

    >>> v1 * 2
    Vector([2.0, 4.0, 6.0])

    >>> 2 * v1
    Vector([2.0, 4.0, 6.0])
    """
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return VectorOverload(a+b for a, b in pairs)
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
    
    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return VectorOverload(n * factor for n in self)
    
    def __rmul__(self, scalar):
        return self * scalar
