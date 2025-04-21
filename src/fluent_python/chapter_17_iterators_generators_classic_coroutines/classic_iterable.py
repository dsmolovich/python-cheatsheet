class IterableList:
    """
    >>> it = IterableList()
    >>> for item in it:
    ...     print(item)
    ...
    A
    B
    10
    abc

    >>> it = IterableList()
    >>> next(it)
    'A'
    >>> next(it)
    'B'
    >>> next(it)
    10
    >>> next(it)
    'abc'
    >>> next(it)
    Traceback (most recent call last):
        ...
    StopIteration
    """
    def __init__(self):
        self._items = ['A', 'B', 10, 'abc']
        self._index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self._items[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration
