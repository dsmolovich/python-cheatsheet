"""
>>> from typing import NamedTuple
>>> class Coordinate(NamedTuple):
...     lon: float
...     lat: float
...     reference: str = 'WGS84'

>>> map_point = Coordinate(3.4567, -2.6456)
>>> map_point
Coordinate(lon=3.4567, lat=-2.6456, reference='WGS84')

>>> Coordinate.__annotations__
{'lon': <class 'float'>, 'lat': <class 'float'>, \
'reference': <class 'str'>}

>>> Coordinate.lon
_tuplegetter(0, 'Alias for field number 0')

>>> Coordinate.__doc__
'Coordinate(lon, lat, reference)'
"""