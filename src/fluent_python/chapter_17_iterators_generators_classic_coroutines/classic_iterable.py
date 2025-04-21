class IterableList:
    """
    >>> iterable_list = IterableList()
    >>> next(iterable_list)
    'A'
    >>> next(iterable_list)
    'B'
    >>> next(iterable_list)
    10
    >>> next(iterable_list)
    'abc'
    >>> next(iterable_list)
    Traceback (most recent call last):
        ...
    StopIteration

    >>> iterable_list = IterableList()
    >>> for item in iterable_list:
    ...     print(item)
    ...
    A
    B
    10
    abc

    """
    def __init__(self):
        self._items = ['A', 'B', 10, 'abc']
        self._index = 0
    
    def __iter__(self):
        return self    

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item
