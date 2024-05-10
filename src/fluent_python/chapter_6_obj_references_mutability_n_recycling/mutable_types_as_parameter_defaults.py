import typing as t

class HauntedBus:
    def __init__(self, passengers:list = []):
        """
        Because "passengers" has a mutable default param []
        this bus becomes "haunted". E.g.

        >>> bus1 = HauntedBus()
        >>> bus1.passengers
        []
        >>> bus1.pick('Charlie')

        >>> bus2 = HauntedBus()
        >>> bus2.passengers # Ooops!
        ['Charlie']

        It's because the default parameter is not [] anymore,
        it is ['Charlie'] now
        >>> HauntedBus.__init__.__defaults__[0]
        ['Charlie']
        >>> HauntedBus.__init__.__defaults__[0] is bus1.passengers
        True
        >>> HauntedBus.__init__.__defaults__[0] is bus2.passengers
        True
        """
        self.passengers = passengers
    
    def pick(self, passenger):
        self.passengers.append(passenger)
    
    def drop(self, passenger):
        self.passengers.remove(passenger)



class TwilightBus:
    def __init__(self, passengers: t.Optional[list] = None):
        """
        Because mutable list club is assigned to self.passengers
        it becomes shared with the world outside of the class. E.g.

        >>> club = ['Alice', 'Bob', 'Charlie', 'David']
        >>> bus = TwilightBus(passengers=club)
        >>> bus.drop('Alice')
        >>> bus.drop('Charlie')

        >>> club # Oops! Alice and Charlie are not in the anymore?
        ['Bob', 'David']

        That's because "bus.passengers" and "club" are labels of the same list:
        >>> bus.passengers is club
        True
        """
        self.passengers = [] if passengers is None else passengers 

    def pick(self, passenger):
        self.passengers.append(passenger)
    
    def drop(self, passenger):
        self.passengers.remove(passenger)



class Bus:
    """
    Now because list() creates a copy of the parameter "passenger"
    the internal "self.passengers" is derefeneced from outside of the class
    the bus behaviour is expected to model the real bus.

    >>> bus1 = Bus()
    >>> bus2 = Bus()

    >>> bus1.pick('Alice')
    >>> bus1.pick('Bob')
    >>> bus2.pick('Charlie')
    >>> bus2.pick('David')
    >>> bus1.passengers
    ['Alice', 'Bob']
    >>> bus2.passengers
    ['Charlie', 'David']

    >>> bus1.drop('Alice')
    >>> bus1.drop('Bob')
    >>> bus2.drop('Charlie')
    >>> bus1.passengers
    []
    >>> bus2.passengers
    ['David']

    >>> club = ['Alice', 'Bob', 'Charlie', 'David']
    >>> bus = Bus(passengers=club)
    >>> bus.drop('Alice')
    >>> bus.drop('Charlie')

    >>> club
    ['Alice', 'Bob', 'Charlie', 'David']

    >>> bus.passengers is club
    False
    """
    def __init__(self, passengers: t.Optional[list] = None):
        self.passengers = [] if passengers is None else list(passengers) 

    def pick(self, passenger):
        self.passengers.append(passenger)
    
    def drop(self, passenger):
        self.passengers.remove(passenger)
