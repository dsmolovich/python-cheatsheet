from p401_vector_take_1_vector2d_compatible import Vector
import operator

def __len__(self: Vector):
    return len(self._components)

def getitem(self: Vector, index):
    return self._components[index]

def _doctest_Vector():
    """
    >>> Vector.__len__ = __len__
    >>> Vector.__getitem__ = getitem

    >>> v = Vector([3, 4, 5])

    >>> len(v)
    3

    >>> v[0], v[-1]
    (3.0, 5.0)

    >>> v7 = Vector(range(7))

    Slicing is not very well supported yet
    >>> v7[1:4]
    array('d', [1.0, 2.0, 3.0])
    """


# slice demo
class MySeq:
    """
    >>> s = MySeq()
    >>> s[1]
    1
    >>> s[1:4]  # 1:4 becomes a slice
    slice(1, 4, None)
    >>> s[1:4:2]
    slice(1, 4, 2)
    >>> s[1:4:2, 9]  # presence of commas inside [] means __getitem__ receives tuple
    (slice(1, 4, 2), 9)
    >>> s[1:4:2, 7:9]  # tuple may hold several slice objects
    (slice(1, 4, 2), slice(7, 9, None))

    >>> slice
    <class 'slice'>
    >>> dir(slice)  # doctest: +ELLIPSIS
    ['__class__', ..., 'indices', ..., 'stop']
    >>> help(slice.indices)
    Help on method_descriptor:
    <BLANKLINE>
    indices(...) unbound builtins.slice method
        S.indices(len) -> (start, stop, stride)
    <BLANKLINE>
        Assuming a sequence of length len, calculate the start and stop
        indices, and the stride length of the extended slice described by
        S. Out of bounds indices are clipped in a manner consistent with the
        handling of normal slices.
    <BLANKLINE>

    >>> slice(None, 10, 2).indices(7)  # 'ABCDE'[:10:2] is the same as 'ABCDE'[0:5:2]
    (0, 7, 2)
    >>> 'ABCDEFG'[:10:2]
    'ACEG'
    >>> 'ABCDEFG'[0:7:2]
    'ACEG'

    >>> slice(-3, None, None).indices(5)  # 'ABCDEFG'[-3:] is the same as 'ABCDEFG'[2:5:1]
    (2, 5, 1)
    >>> 'ABCDEFG'[-3:]
    'EFG'
    >>> 'ABCDEFG'[4:7:1]
    'EFG'
    """
    def __getitem__(self, index):
        return index


def slice_aware_getitem(self: Vector, key):
    if(isinstance(key, slice)):
        cls = type(self)
        return cls(self._components[key])
    index = operator.index(key)
    return self._components[index]

def _doctest_slice_aware_Vector():
    """
    >>> Vector.__getitem__ = slice_aware_getitem
    >>> v = Vector(range(7))

    >>> v[-1]
    6.0

    >>> v[1:4]
    Vector([1.0, 2.0, 3.0])

    >>> v[-1:]
    Vector([6.0])

    >>> v[1,2]
    Traceback (most recent call last):
        ...
    TypeError: 'tuple' object cannot be interpreted as an integer
    """
