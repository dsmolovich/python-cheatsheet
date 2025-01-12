import functools
import operator
from collections.abc import Iterable
from typing import overload, Union, TypeVar

T = TypeVar('T')
S = TypeVar('S')

@overload
def sum(it: Iterable[T]) -> Union[T, int]: ...
@overload
def sum(it: Iterable[T], /, start: S) -> Union[T, S]: ...
def sum(it, /, start=0):
    """
    The / in a function definition indicates that the arguments before it are positional-only

    >>> sum([1,2,3])
    6
    >>> sum([1,2,3], 10)
    16

    >>> sum(it=[1,2,3])
    Traceback (most recent call last):
        ...
    TypeError: sum() got some positional-only arguments passed as keyword arguments: 'it'
    """
    return functools.reduce(operator.add, it, start)

sum([1,2,3])
sum([1,2,3], 10)

# mypy will complain on the next code:
#   sum(1, 2)
# with the next error:
#   error: No overload variant of "sum" matches argument types "int", "int"  [call-overload]
