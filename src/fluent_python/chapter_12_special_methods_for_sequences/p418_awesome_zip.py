"""
>>> zip(range(3), 'ABC')  # doctest: +ELLIPSIS
<zip object at 0x...

>>> list(zip(range(3), 'ABC'))
[(0, 'A'), (1, 'B'), (2, 'C')]

>>> list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))
[(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]

>>> from itertools import zip_longest
>>> list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue = -1))
[(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]

Transposing matrix:
>>> a = [(1,2,3),
...      (4,5,6)]

>>> list(zip(*a))
[(1, 4), (2, 5), (3, 6)]

>>> a = [(1,2),
...      (3,4),
...      (5,6)]

>>> list(zip(*a))
[(1, 3, 5), (2, 4, 6)]
"""