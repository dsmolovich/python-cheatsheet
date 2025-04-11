import sys

class LookingGlass:
    """
    >>> with LookingGlass() as what:
    ...     print('Alice, Kitty and Snowdrop')
    ...     print(what)
    ...     print(1/0)
    ...
    pordwonS dna yttiK ,ecilA
    ykcowrebbaJ
    Please DO NOT divide by zero!

    >>> what
    'Jabberwocky'

    >>> print('Back to normal.')
    Back to normal.

    >>> context_manager = LookingGlass()
    >>> context_manager # doctest: +ELLIPSIS
    <...LookingGlass object at ...>
    
    >>> monster = context_manager.__enter__()
    
    >>> monster == 'Jabberwocky'
    eurT
    
    >>> monster
    'ykcowrebbaJ'
    
    >>> context_manager # doctest: +ELLIPSIS
    >... ta tcejbo ssalGgnikooL...<

    >>> print('abc')
    cba

    >>> context_manager.__exit__(None, None, None)
    >>> monster
    'Jabberwocky'
    """
    def __enter__(self):
        self.oroginal_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'Jabberwocky'
    
    def reverse_write(self, text: str):
        self.oroginal_write(text[::-1])
    
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.oroginal_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
