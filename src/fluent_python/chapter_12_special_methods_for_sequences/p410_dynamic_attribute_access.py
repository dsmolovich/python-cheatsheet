from array import array
from typing import Any
import reprlib

class Vector:
    """
    >>> v = Vector(range(10))
    >>> v.x
    0.0
    >>> v.y, v.z, v.t
    (1.0, 2.0, 3.0)
    >>> v
    Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
    >>> v.x = 10
    Traceback (most recent call last):
        ...
    AttributeError: readonly attribute 'x'
    """

    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg =  f'{cls.__name__} object has no attribute {name!r}'
        raise ArithmeticError(msg)

    def __setattr__(self, name: str, value: Any) -> None:
        cls = type(self)
        if len(name) == 1:
            error = ''
            if name in cls.__match_args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            if error:
                msg = error.format(cls_name = cls.__name__, attr_name = name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'{type(self).__name__}({components})'
