from collections.abc import Generator

def averager() -> Generator[float, float, None]:
    """
    >>> coro_avg = averager()
    
    Start the coroutine
    >>> next(coro_avg)
    0.0

    Each call to .send() yields the current average
    >>> coro_avg.send(10)
    10.0

    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

    Terminating infinite loop (not required as the coroutine will be garbage collected)
    >>> coro_avg.close()
    >>> coro_avg.close()
    >>> coro_avg.close() # can be called any times
    >>> coro_avg.send(5)
    Traceback (most recent call last):
        ...
    StopIteration
    """
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
