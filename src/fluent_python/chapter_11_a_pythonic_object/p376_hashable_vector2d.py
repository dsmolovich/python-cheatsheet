class Vector2d:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __iter__(self):
        return (i for i in (self.x, self.y))

def _doctest_it():
    """
    >>> v1 = Vector2d(3, 4)
    >>> v2 = Vector2d(3.1, 4.1)
    
    >>> hash(v1), hash(v2)
    (1079245023883434373, 4933425947639606603)

    >>> {v1, v2}
    {Vector2d(3.1, 4.1), Vector2d(3, 4)}
    """
