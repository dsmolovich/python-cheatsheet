def _doctest_format():
    """
    >>> brl = 1 / 4.28
    >>> brl
    0.2336448598130841

    >>> format(brl, '0.4f')
    '0.2336'

    >>> '1 BRL = {rate:0.2f} USD'.format(rate=brl)
    '1 BRL = 0.23 USD'

    >>> f'1 USD = {1 / brl:0.2f} BRL'
    '1 USD = 4.28 BRL'

    >>> format(42, 'b') # binary
    '101010'

    >>> format(42, 'x') # hex
    '2a'

    >>> format(2 / 3, '.1%') # percent
    '66.7%'
    """



import math
from p369_vector_class_redux import Vector2d

def format_ext(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self)
    return '({}, {})'.format(*components)

# dynamically extend class with the method
setattr(Vector2d, '__format__', format_ext)

def _doctest_extended_Vector2d():
    """
    >>> v1 = Vector2d(3, 4)
    >>> format(v1)
    '(3.0, 4.0)'

    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'
    """

# Adding formatting with polar coordinates (format spec = '...p')
def angle(self):
    return math.atan2(self.y, self.x)

def format_ext_polar_cooords(self, fmt_spec=''):
    if fmt_spec.endswith('p'):
        fmt_spec = fmt_spec[:-1]
        coords = (abs(self), self.angle())
        outer_fmt = '<{}, {}>'
    else:
        coords = self
        outer_fmt = '({}, {})'
    components = (format(c, fmt_spec) for c in coords)
    return outer_fmt.format(*components)

setattr(Vector2d, 'angle', angle)
setattr(Vector2d, '__format__', format_ext_polar_cooords)

def _doctest_polar_coords():
    """
    >>> v1 = Vector2d(1, 1)

    >>> format(v1, 'p')
    '<1.4142135623730951, 0.7853981633974483>'

    >>> format(v1, '.3ep')
    '<1.414e+00, 7.854e-01>'

    >>> format(v1, '.5fp')
    '<1.41421, 0.78540>'
    """
