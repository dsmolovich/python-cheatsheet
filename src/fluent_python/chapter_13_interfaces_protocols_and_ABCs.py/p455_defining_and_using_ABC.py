import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add item from iterable"""
    
    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random, returning it
        
        This method should raise LookupError when the instance is empty
        """
    
    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise"""
        return bool(self.inspect())
    
    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick)
            except LookupError:
                break
        self.load(items)
        return tuple(items)

class Fake(Tombola):
    """
    >>> Fake
    <class 'p455_defining_and_using_ABC.Fake'>

    >>> f = Fake()
    Traceback (most recent call last):
    ...
    TypeError: Can't instantiate abstract class Fake without an implementation for abstract method 'load'
    """
    def pick(self):
        return 13

# Virtual Subclass:
from random import randrange

@Tombola.register
class TomboList(list):
    """
    >>> issubclass(TomboList, Tombola)
    True

    >>> t = TomboList(range(100))
    >>> isinstance(t, Tombola)
    True

    Method Resolution Order (MRO)
    >>> TomboList.__mro__
    (<class 'p455_defining_and_using_ABC.TomboList'>, <class 'list'>, <class 'object'>)
    """
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty Tombolist')

    load = list.extend # TomboList load() is the same as list.extend()

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)

#Tombola.register(TomboList) # Alternative way of registering virtual subclass. Used prior to Python 3.3
