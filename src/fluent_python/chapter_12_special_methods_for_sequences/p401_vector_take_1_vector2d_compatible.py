from array import array
import reprlib
import math

class Vector:
    """
    >>> Vector([3.1, 4.2])
    Vector([3.1, 4.2])

    >>> Vector([3, 4, 5])
    Vector([3.0, 4.0, 5.0])

    >>> Vector(range(10, 20, 2))
    Vector([10.0, 12.0, 14.0, 16.0, 18.0])
    """
    typecode = 'd'

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'{type(self).__name__}({components})'
    
    def __str__(self) -> str:
        return str(tuple(self))

    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
