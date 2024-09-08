from p376_hashable_vector2d import Vector2d

def _doctest_it():
    """
    >>> v = Vector2d(3, 4)
    
    >>> v.__dict__
    {'_Vector2d__x': 3, '_Vector2d__y': 4}

    >>> v._Vector2d__x
    3
    """