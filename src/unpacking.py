metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    """
    >>> main()
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


if __name__ == '__main__':
    main()