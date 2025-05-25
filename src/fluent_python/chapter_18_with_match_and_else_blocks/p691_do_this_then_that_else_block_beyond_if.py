from logging import log, ERROR, INFO
import os

def for_else(items: list[str]):
    """
    >>> items = ['apple', 'strawberry', 'banana']
    >>> for_else(items)
    'banana'

    >>> items = ['apple', 'strawberry']
    >>> for_else(items) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: No banana found in the list
    """

    for item in items:
        if item == 'banana':
            break
    else:
        raise ValueError('No banana found in the list')
    return item


def while_else():
    """
    >>> while_else()
    1
    2
    3
    4
    5
    i is no longer less than 6
    End
   """
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")
    print('End')


def try_else(path: str):
    """
    >>> try_else('/tmp')
    All good
    End

    >>> try_else('/non/existing/path')
    OSError...
    End
    """
    try:
        os.listdir(path)
    except OSError:
        print('OSError...')
    else:
        print('All good')
    print('End')
