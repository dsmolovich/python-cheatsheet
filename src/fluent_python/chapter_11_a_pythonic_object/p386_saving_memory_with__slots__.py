class Pixel:
    """
    >>> p = Pixel()

    >>> p.__dict__
    Traceback (most recent call last):
        ...
    AttributeError: 'Pixel' object has no attribute '__dict__'. Did you mean: '__dir__'?
    """
    __slots__ = ('x', 'y')


class OpenPixel(Pixel):
    """"
    >>> op = OpenPixel()

    >>> op.__dict__
    {}

    >>> op.x = 8
    >>> op.__dict__
    {}
    >>> op.x
    8

    >>> op.color = 'green'
    >>> op.__dict__
    {'color': 'green'}
    """
    pass

class ColorPixel(Pixel):
    """
    >>> cp = ColorPixel()

    >>> cp.x, cp.y, cp.color = 8, 12, 'blue'
    >>> cp.x, cp.y, cp.color
    (8, 12, 'blue')

    >>> cp.flavour = 'banana'
    Traceback (most recent call last):
        ...
    AttributeError: 'ColorPixel' object has no attribute 'flavour'
    """
    __slots__ = ('color',)
