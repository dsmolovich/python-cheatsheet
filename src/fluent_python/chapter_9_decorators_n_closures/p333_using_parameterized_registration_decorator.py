"""
>>> from src.fluent_python.chapter_9_decorators_n_closures.p331_parameterized_registration_decorator import *  #doctest: +ELLIPSIS
running register(active=False)->decorate(<function f1 at 0x...>)
running register(active=True)->decorate(<function f2 at 0x...>)

>>> registry  #doctest: +ELLIPSIS
{<function f2 at 0x...>}

>>> register()(f3)  #doctest: +ELLIPSIS
running register(active=True)->decorate(<function f3 at 0x...>)
<function f3 at 0x...>

>>> registry  #doctest: +ELLIPSIS
{<function f2 at 0x...>, <function f3 at 0x...>}

>>> register(active = False)(f2)  #doctest: +ELLIPSIS
running register(active=False)->decorate(<function f2 at 0x...>)
<function f2 at 0x...>

>>> registry  #doctest: +ELLIPSIS
{<function f3 at 0x...>}
"""