class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')

class Leaf(A, B):
    """
    >>> leaf = Leaf()

    >>> leaf.ping()
    <instance of Leaf>.ping() in Leaf
    <instance of Leaf>.ping() in A
    <instance of Leaf>.ping() in B
    <instance of Leaf>.ping() in Root

    >>> leaf.pong()
    <instance of Leaf>.pong() in A
    <instance of Leaf>.pong() in B

    >>> Leaf.__mro__ # doctest: +NORMALIZE_WHITESPACE
    (<class 'p496_multiple_inheritance_and_method_resolution_order.Leaf'>,
     <class 'p496_multiple_inheritance_and_method_resolution_order.A'>,
     <class 'p496_multiple_inheritance_and_method_resolution_order.B'>,
     <class 'p496_multiple_inheritance_and_method_resolution_order.Root'>,
     <class 'object'>)
    """
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()
