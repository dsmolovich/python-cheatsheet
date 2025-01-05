def double(x):
    """
    >>> double(1.5)
    3.0

    >>> double('A')
    'AA'

    >>> double([10, 20, 30])
    [10, 20, 30, 10, 20, 30]

    >>> from fractions import Fraction
    >>> double(Fraction(2, 5))
    Fraction(4, 5)

    >>> from src.fluent_python.chapter_1_python_data_model.p11_vectors import Vector
    >>> double(Vector(x=11.0, y=12.0))
    Vector(22.0, 24.0)
    """
    return x*2


from typing import TypeVar, Protocol

T = TypeVar('T')

class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T:
        ...

RT = TypeVar('RT', bound=Repeatable)

def typed_double(x: RT) -> RT:
    """
    >>> typed_double(1.5)
    3.0

    >>> typed_double('A')
    'AA'

    >>> typed_double([10, 20, 30])
    [10, 20, 30, 10, 20, 30]

    >>> from fractions import Fraction
    >>> typed_double(Fraction(2, 5))
    Fraction(4, 5)

    >>> from src.fluent_python.chapter_1_python_data_model.p11_vectors import Vector
    >>> double(Vector(x=11.0, y=12.0))
    Vector(22.0, 24.0)
    """
    return x * 2
