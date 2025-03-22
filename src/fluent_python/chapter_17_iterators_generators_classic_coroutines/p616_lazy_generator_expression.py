def gen_AB():
    """
    Eager (comprehension list):
    >>> res1 = [x*3 for x in gen_AB()]
    start
    continue
    end
    >>> for i in res1:
    ...     print('-->',i)
    ...
    --> AAA
    --> BBB

    Lazy (generator):
    >>> res2 = (x*3 for x in gen_AB())
    >>> for i in res2:
    ...     print('-->',i)
    ...
    start
    --> AAA
    continue
    --> BBB
    end
    """
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

