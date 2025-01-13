from collections.abc import Callable, Iterable
from typing import Protocol, Any, TypeVar, overload, Union

class SupportsLessThen(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar('T')
LT = TypeVar('LT', bound=SupportsLessThen)
DT = TypeVar('DT')

MISSING = object()
EMPTY_MSG = 'max() arg is an empty sequence'

@overload
def max(__arg1: LT, __arg2: LT, *args: LT, key: None = ...) -> LT:
    """ (1) Agruments supporting SupportsLessThan but key and default not provided """
@overload
def max(__iterable: Iterable[LT], *, key: None = ...) -> LT:
    """ (1) Agruments supporting SupportsLessThan but key and default not provided """
@overload
def max(__arg1: T, __arg2: T, *args: T, key: Callable[[T], LT]) -> T:
    """ (2) Agrument key provided but no default """
@overload
def max(__iterable: Iterable[T], *, key: Callable[[T], LT]) -> T:
    """ (2) Agrument key provided but no default """
@overload
def max(__iterable: Iterable[LT], *, key: None = ..., default: DT) -> Union[LT, DT]:
    """ (3) Argument default provided but no key """
@overload
def max(__iterable: Iterable[T], *, key: Callable[[T], LT], default: DT) -> Union[T, DT]:
    """ (4) Argument key and default provided """

def max(first, *args, key=None, default=MISSING):
    """
    >>> max(1, 2)
    2

    (1) Agruments supporting SupportsLessThan but key and default not provided:
    >>> max(1, 2, -3)
    2
    >>> max(1, 2, -3, 4, 5)
    5
    >>> max(['Go', 'Python', 'Rust'])
    'Rust'

    (2) Agrument key provided but no default:
    >>> max(1, 2, -3, key=abs)
    -3
    >>> max(['Go', 'Python', 'Rust'], key=len)
    'Python'

    (3) Argument default provided but no key:
    >>> max([1, 2, -3], default=0)
    2
    >>> max([], default=0)
    0

    (4) Argument key and default provided:
    >>> max(1, 2, -3, key=abs, default=None)
    -3
    >>> 
    >>> max([], key=abs, default=0)
    0
    """
    if args:
        series = args
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(EMPTY_MSG) from None
    if key is None:
        for current in series:
            if candidate < current:
                candidate = current
    else:
        candidate_key = key(candidate)
        for current in series:
            current_key = key(current)
            if candidate_key < current_key:
                candidate = current
                candidate_key = current_key
    return candidate

max(1,2)
max(1,2,-3)
max(['Go', 'Python', 'Rust'])
max(1, 2, -3, key=abs)
max(['Go', 'Python', 'Rust'], key=len)
max([1, 2, -3], default=0)
max([], default=0)
max([1, 2, -3], key=abs, default=None)
max([], key=abs, default=0)
