"""
>>> def deco(func):
...    def inner():
...        print('running inner()')
...    return inner
...
>>> @deco
... def target():
...     print('running target()')
...
>>> target()
running inner()
>>> target  #doctest: +ELLIPSIS
<function deco.<locals>.inner at 0x...>

>>> target = deco(target)
>>> target()
running inner()
>>> target  #doctest: +ELLIPSIS
<function deco.<locals>.inner at 0x...>
"""
