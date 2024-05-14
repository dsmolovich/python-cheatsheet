"""
>>> def factorial(n):
...     "returns n!"
...     return 1 if n < 2 else n * factorial(n-1)
...

>>> factorial(42)
1405006117752879898543142606244511569936384000000000

>>> factorial.__doc__
'returns n!'

>>> map(factorial, range(11))
<map object at 0x10697be80>
>>> list(map(factorial, range(11)))
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
"""
