"""
>>> def factorial(n):
...     "returns n!"
...     return 1 if n < 2 else n * factorial(n-1)
...


Map and Filter:

>>> map(factorial, range(6)) # doctest: +ELLIPSIS
<map object at ...>
>>> list(map(factorial, range(6)))
[1, 1, 2, 6, 24, 120]

>>> list(map(factorial, filter(lambda n: n%2, range(6))))
[1, 6, 120]

>>> [factorial(n) for n in range(6) if n %2]
[1, 6, 120]


Reduce:

>>> from functools import reduce
>>> from operator import add

>>> reduce(add, range(5))
10

>> sum(range(5))
10
"""
