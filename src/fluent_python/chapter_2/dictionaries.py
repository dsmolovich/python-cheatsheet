"""
Dictionaries:

>>> dial_codes = [
...    (800, 'Bangladesh'),
...    (55, 'Brazil'),
...    (86, 'China'),
...    (91, 'India'),
...    (62, 'Indonesia'),
...    (81, 'Japan'),
...    (234, 'Nigeria'),
...    (92, 'Pakistan'),
...    (7, 'Russia'),
...    (1, 'United States'),
... ]

>>> country_dial = {country: code for code, country in dial_codes}
>>> country_dial
{'Bangladesh': 800, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, \
'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}

>>> {code: country.upper() 
...     for country, code in sorted(country_dial.items())
...     if code < 70}
{55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}

>>> {code: country.upper() 
...     for code, country in sorted(dial_codes)
...     if code < 70}
{1: 'UNITED STATES', 7: 'RUSSIA', 55: 'BRAZIL', 62: 'INDONESIA'}

Unpacking mappings:

>>> def dump(**kwargs):
...     return kwargs
...
>>> dump(**{'x': 1}, y=2, **{'z': 3})
{'x': 1, 'y': 2, 'z': 3}

>>> {'a': 0, **{'x': 1}, 'y':2, **{'z': 3, 'x': 4} }
{'a': 0, 'x': 4, 'y': 2, 'z': 3}

>>> {'a': 0, **{'b': 1, **{'c': 2, **{'d': 3, **{'b': 100}}}}}
{'a': 0, 'b': 100, 'c': 2, 'd': 3}


Merging mappings:

>>> d1 = {'a': 0, 'b': 1}
>>> d2 = {'a': 2, 'b': 3, 'c': 4}

>>> d1 | d2
{'a': 2, 'b': 3, 'c': 4}

>>> d1 |= d2
>>> d1
{'a': 2, 'b': 3, 'c': 4}
"""

# Pattern matching with mappings:
def get_creators(record: dict) -> list:
    """
    >>> b1 = dict(api=1, author='Douglas Hofstradter',
    ...     type='book', title='Godel, Escher, Bach')
    >>> get_creators(b1)
    ['Douglas Hofstradter']

    >>> from collections import OrderedDict
    >>> b2 = OrderedDict(api=2, type='book', title='Python in a nutshell',
    ...         authors='Martelly Ravenscroft Holden'.split())
    >>> get_creators(b2)
    ['Martelly', 'Ravenscroft', 'Holden']

    >>> get_creators({'type': 'book', 'pages': 1024})
    Traceback (most recent call last):
        ...
    ValueError: Invalid 'book' record: {'type': 'book', 'pages': 1024}
    """
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")
