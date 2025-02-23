from re import compile
from reprlib import repr

RE_WORD = compile(r'\w+')

class Sentence:
    """
    >>> s = Sentence('"The time has come," the Walrus said,')
    
    >>> s
    Sentence('"The time ha... Walrus said,')

    >>> for word in s:
    ...     print(word)
    The
    time
    has
    come
    the
    Walrus
    said

    >>> list(s)
    ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']

    >>> s[0]
    'The'
    >>> s[5]
    'Walrus'
    >>> s[-1]
    'said'
    """

    def __init__(self, text: str) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self) -> int:
        return len(self.words)
    
    def __repr__(self) -> str:
        return 'Sentence(%s)' % repr(self.text)
