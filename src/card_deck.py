# Fluent Python
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'Spades Diamonds Clubs Hearts'.split(' ')
    
    def __init__(self):
        self._cards = [Card(rank, suit)
                      for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    deck = FrenchDeck()
    for i in range(0, 6):
        card = choice(deck)
        print(card)
