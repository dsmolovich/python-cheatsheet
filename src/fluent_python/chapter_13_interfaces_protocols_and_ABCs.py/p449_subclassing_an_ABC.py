from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(abc.MutableSequence):
    """
    >>> deck = FrenchDeck()

    >>> len(deck)
    52
    
    >>> deck[0]
    Card(rank='2', suit='spades')

    >>> deck[-1]
    Card(rank='A', suit='hearts')

    >>> deck[0], deck[-1] = deck[-1], deck[0]
    >>> deck[0], deck[-1]
    (Card(rank='A', suit='hearts'), Card(rank='2', suit='spades'))

    >>> del deck[0]
    >>> len(deck)
    51

    >>> deck[0], deck[1], deck[2]
    (Card(rank='3', suit='spades'), Card(rank='4', suit='spades'), Card(rank='5', suit='spades'))
    >>> deck.insert(1, Card(rank='A', suit='hearts'))
    >>> len(deck)
    52
    >>> deck[0], deck[1], deck[2]
    (Card(rank='3', suit='spades'), Card(rank='A', suit='hearts'), Card(rank='4', suit='spades'))
    """
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)
