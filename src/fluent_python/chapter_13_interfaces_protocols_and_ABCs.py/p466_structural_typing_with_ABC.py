class Struggle:
    """
    >>> from collections import abc
    >>> isinstance(Struggle(), abc.Sized)
    True
    >>> issubclass(Struggle, abc.Sized)
    True
    """
    def __len__(self):
        return 23

