from p369_vector_class_redux import Vector2d

def keyword_pattern_demo(v: Vector2d):
    """
    >>> keyword_pattern_demo(Vector2d(0, 0))
    Vector2d(0.0, 0.0) is null
    
    >>> keyword_pattern_demo(Vector2d(0, 15))
    Vector2d(0.0, 15.0) is vertical

    >>> keyword_pattern_demo(Vector2d(15, 0))
    Vector2d(15.0, 0.0) is horizontal

    >>> keyword_pattern_demo(Vector2d(15, -15))
    Vector2d(15.0, -15.0) is diagonal

    >>> keyword_pattern_demo(Vector2d(2, 3))
    Vector2d(2.0, 3.0) is just a regular vector
    """
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'{v!r} is vertical')
        case Vector2d(y=0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if abs(x) == abs(y):
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is just a regular vector')


def positional_pattern_demo(v: Vector2d):
    """
    >>> positional_pattern_demo(Vector2d(0, 0))
    Vector2d(0.0, 0.0) is null
        
    >>> positional_pattern_demo(Vector2d(0, 15))
    Vector2d(0.0, 15.0) is vertical

    >>> positional_pattern_demo(Vector2d(15, 0))
    Vector2d(15.0, 0.0) is horizontal

    >>> positional_pattern_demo(Vector2d(15, -15))
    Vector2d(15.0, -15.0) is diagonal

    >>> positional_pattern_demo(Vector2d(2, 3))
    Vector2d(2.0, 3.0) is just a regular vector
    """

    # set __match_args__ class attribute to make positional
    setattr(Vector2d, '__match_args__', ('x', 'y'))

    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if abs(x) == abs(y):
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is just a regular vector')
