import contextlib
import sys

@contextlib.contextmanager
def looking_glass():
    """
    >>> with looking_glass() as what:
    ...     print('Alice, Kitty and Snowdrop')
    ...     print(what)
    ...
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ

    >>> what
    'JABBERWOCKY'
    """
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
