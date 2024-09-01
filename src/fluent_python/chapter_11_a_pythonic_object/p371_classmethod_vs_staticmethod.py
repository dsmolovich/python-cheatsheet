class Demo:
    @staticmethod
    def statmeth(*args):
        return args

    @classmethod
    def klassmeth(*args):
        return args


def _doctest_it():
    """
    >>> Demo.statmeth()
    ()
    >>> Demo.statmeth('spam')
    ('spam',)
    >>> Demo.statmeth('some', 'spam')
    ('some', 'spam')

    >>> Demo.klassmeth()
    (<class 'p371_classmethod_vs_staticmethod.Demo'>,)
    >>> Demo.klassmeth('spam')
    (<class 'p371_classmethod_vs_staticmethod.Demo'>, 'spam')
    >>> Demo.klassmeth('some', 'spam')
    (<class 'p371_classmethod_vs_staticmethod.Demo'>, 'some', 'spam')
    """