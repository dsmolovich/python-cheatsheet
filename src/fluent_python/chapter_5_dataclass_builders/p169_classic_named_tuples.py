"""
>>> from collections import namedtuple

>>> # Able to take iterable as fields:
>>> City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
>>> # or string separated with spaces:
>>> City = namedtuple('City', 'name country population coordinates')

>>> tokyo = City('Tokyo', 'JP', 36_933, (35.689733, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36933, coordinates=(35.689733, 139.691667))
>>> tokyo.population
36933
>>> tokyo.coordinates
(35.689733, 139.691667)

>>> City._fields
('name', 'country', 'population', 'coordinates')

>>> Coordinate = namedtuple('Coordinate', 'lat lon')
>>> delhi_data = City('Delhi', 'IN', 21_935, Coordinate(28.613889, 77.208889))
>>> delhi = City._make(delhi_data)
>>> delhi._asdict()
{'name': 'Delhi', 'country': 'IN', 'population': 21935, \
'coordinates': Coordinate(lat=28.613889, lon=77.208889)}

>>> import json
>>> json.dumps(delhi._asdict())
'{"name": "Delhi", "country": "IN", "population": 21935, \
"coordinates": [28.613889, 77.208889]}'

>>> Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
>>> Coordinate(0, 0)
Coordinate(lat=0, lon=0, reference='WGS84')
>>> Coordinate._field_defaults
{'reference': 'WGS84'}

>>> Province = namedtuple('State', 'name country')
>>> ontario = Province('Ontario', 'CA')
>>> ontario
State(name='Ontario', country='CA')
"""
