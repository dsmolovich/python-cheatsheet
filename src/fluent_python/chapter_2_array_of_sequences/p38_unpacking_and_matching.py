# Nested unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def nested_unpacking():
    """
    >>> nested_unpacking()
    City            |     Latitude |    Longitude
    ---------------------------------------------
    Mexico City     |    19.433333 |   -99.133333
    New York-Newark |    40.808611 |   -74.020386
    São Paulo       |   -23.547778 |   -46.635833
    """

    print(f"{'City':15} | {'Latitude':>12} | {'Longitude':>12}")
    print("-" * 45)
    for name, *_, (lat, lon) in metro_areas:
        if lon < 0:
            print(f"{name:15} | {lat:>12} | {lon:>12}")

# Matching
class Coord:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

metro_areas_with_obj = [
    ('Tokyo', 'JP', 36.933, Coord(35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, Coord(28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, Coord(19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, Coord(40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, Coord(-23.547778, -46.635833)),
]

def matching():
    """
    >>> matching()
    City            |     Latitude |    Longitude
    ---------------------------------------------
    Mexico City     |    19.433333 |   -99.133333
    New York-Newark |    40.808611 |   -74.020386
    São Paulo       |   -23.547778 |   -46.635833
    """

    print(f"{'City':15} | {'Latitude':>12} | {'Longitude':>12}")
    print("-" * 45)
    for record in metro_areas_with_obj:
        match record:
            case [name, _, _, Coord() as coord] if coord.lon < 0:
                print(f"{name:15} | {coord.lat:>12} | {coord.lon:>12}")


if __name__ == '__main__':
    nested_unpacking()
    print("=" * 45)
    matching()