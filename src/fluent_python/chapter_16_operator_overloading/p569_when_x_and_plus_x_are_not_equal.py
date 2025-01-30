import decimal

def _test_if():
    """
    >>> ctx = decimal.getcontext()
    >>> ctx.prec = 40

    >>> one_third = decimal.Decimal(1) / decimal.Decimal(3)
    >>> one_third
    Decimal('0.3333333333333333333333333333333333333333')

    >>> one_third == +one_third
    True

    >>> ctx.prec=2
    >>> one_third == +one_third
    False

    >>> one_third
    Decimal('0.3333333333333333333333333333333333333333')

    >>> +one_third
    Decimal('0.33')
    """
