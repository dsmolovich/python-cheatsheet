"""
A multidimential Vector

Init tests:
    >>> Vector([3.1, 4.2])
    Vector([3.1, 4.2])
    >>> Vector([3, 4, 5])
    Vector([3.0, 4.0, 5.0])
    >>> Vector(range(10))
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

2D vector tests:
    >>> v1 = Vector([3, 4])
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1_clone = eval(repr(v1))
    >>> v1_clone == v1
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector([0, 0]))
    (True, False)

Test of .frombytes() method
    >>> v1_clone = Vector.frombytes(bytes(v1))
    >>> v1_clone
    Vector([3.0, 4.0])
    >>> v1 == v1_clone
    True

3D vector tests:
    >>> v1 = Vector([3, 4, 5])
    >>> x, y, z = v1
    >>> x, y, z
    (3.0, 4.0, 5.0)
    >>> v1
    Vector([3.0, 4.0, 5.0])
    >>> v1_clone = eval(repr(v1))
    >>> v1_clone == v1
    True
    >>> print(v1)
    (3.0, 4.0, 5.0)
    >>> abs(v1)
    7.0710678118654755
    >>> bool(v1), bool(Vector([0, 0, 0]))
    (True, False)

Higher dimensions tests:
    >>> v7 = Vector(range(7))
    >>> v7
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> abs(v7)
    9.539392014169456
    >>> v7_clone = Vector.frombytes(bytes(v7))
    >>> v7_clone
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> v7 == v7_clone
    True

Sequence behaviour tests:
    >>> v1 = Vector([3, 4, 5])
    >>> v1[0], v1[len(v1)-1], v1[-1]
    (3.0, 5.0, 5.0)

Slicing tests:
    >>> v7 = Vector(range(7))
    >>> v7[-1]
    6.0
    >>> v7[1:4]
    Vector([1.0, 2.0, 3.0])
    >>> v7[-1:]
    Vector([6.0])
    >>> v7[1,2]
    Traceback (most recent call last):
    ...
    TypeError: 'tuple' object cannot be interpreted as an integer

Dynamic attribute access tests:    
    >>> v7 = Vector(range(7))
    >>> v7.x
    0.0
    >>> v7.y, v7.z, v7.t
    (1.0, 2.0, 3.0)
    >>> v7.k
    Traceback (most recent call last):
    ...
    AttributeError: 'Vector' object has no attribute 'k'
    
Hashing tests:
    >>> v1 = Vector([3, 4])
    >>> v2 = Vector([3.1, 4.2])
    >>> v3 = Vector([3, 4, 5])
    >>> v6 = Vector(range(6))
    >>> hash(v1), hash(v2), hash(v3), hash(v6)
    (7, 384307168202284039, 2, 1)

Format tests:
    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'
    >>> format(v1, 'h')
    '<5.0, 0.9272952180016122>'
    >>> format(Vector([2, 3, 4]))
    '(2.0, 3.0, 4.0)'
    >>> v3 = Vector([2, 3, 4])
    >>> format(v3, 'h')
    '<5.385164807134504, 1.1902899496825317, 0.9272952180016122>'
    >>> format(v3, '.3fh')
    '<5.385, 1.190, 0.927>'
    >>> format(v3, '.3eh')
    '<5.385e+00, 1.190e+00, 9.273e-01>'
    >>> format(Vector([-1, -1, -1]), 'h')
    '<1.7320508075688772, 2.186276035465284, 3.9269908169872414>'
"""

from array import array 
import reprlib
import math
import functools
import operator
import itertools

class Vector:
    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components) -> None:
        self._components = array(self. typecode, components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'
    
    def  __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components)) 

    def __len__(self):
        return len(self._components)

    def __eq__(self, other) -> bool:
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))
    
    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]
    
    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)
    
    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if (n == len(self) -1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec: str) -> str:
        if fmt_spec.endswith('h'): # hyperspherical coords
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
