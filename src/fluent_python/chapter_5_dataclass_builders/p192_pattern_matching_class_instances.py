"""
======================
Simple Class Patterns

>>> file = [
...     ("Toronto", "ON", "CA", (43.7, -79.4)),
...     ("New York", "NY", "US", (40.7, -74.0)),
...     ("Apple", 1.99, 'lb'),
...     ("Tokyo", "TY", "JP", (35.7, 139.7)),
...     (52.5, 13.4, 17.25, (2.33, -5.45)),
...     (['a','b','c'], "RM", "IT", (41.9, 12.5)),
...     ("Moscow", "MOW", "RU", (55.8, 37.6)),
...     ("Cherry", 3.99, 'kg'),
...     ("Beijing", "BJ", "CN", (39.9, 116.4))
... ]
>>> cities, products, etc = [], [], []
>>> for record in file:
...     match record:
...         case [str(name), _, _, (float(lat), float(lon))]:
...             cities.append((name, lat, lon))
...         case [str(name), float(price), str(unit)]:
...             products.append((name, f"{price}/{unit}"))
...         case _:
...             etc.append(record)

>>> cities
[('Toronto', 43.7, -79.4), ('New York', 40.7, -74.0), \
('Tokyo', 35.7, 139.7), ('Moscow', 55.8, 37.6), ('Beijing', 39.9, 116.4)]

>>> products
[('Apple', '1.99/lb'), ('Cherry', '3.99/kg')]

>>> etc
[(52.5, 13.4, 17.25, (2.33, -5.45)), \
(['a', 'b', 'c'], 'RM', 'IT', (41.9, 12.5))]



======================
Keyword Class Patterns

>>> import typing
>>> class City(typing.NamedTuple):
...     continent: str
...     name: str
...     country: str


>>> cities = [
...     City('Asia', 'Tokyo', 'JP'),
...     City('Asia', 'Delhi', 'IN'),
...     City('North America', 'Mexico City', 'MX'),
...     City('North America', 'New York', 'US'),
...     City('South America', 'São Paolo', 'BR'),
...     City('South America', 'Rio de Janeiro', 'BR'),
... ]

>>> cities_in_asia, cities_in_brazil = [], []
>>> for city in cities:
...     match city:
...         case City(continent='Asia'):
...             cities_in_asia.append(city)
...         case City(name=city_name, country='BR'):
...             cities_in_brazil.append(city_name)

>>> cities_in_asia
[City(continent='Asia', name='Tokyo', country='JP'), \
City(continent='Asia', name='Delhi', country='IN')]

>>> cities_in_brazil
['São Paolo', 'Rio de Janeiro']


======================
Positional Class Patterns

>>> asian_countries = []
>>> for city in cities:
...     match city:
...         case City('Asia', _, country):
...             asian_countries.append(country)

>>> asian_countries
['JP', 'IN']
"""