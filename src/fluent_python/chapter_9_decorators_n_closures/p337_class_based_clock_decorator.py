import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

class clock:
    def __init__(self, fmt = DEFAULT_FMT):
        self._fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self._fmt.format(**locals()))
            return _result
        return clocked


@clock(fmt = '{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


def _doctest_it():
    """
    >>> for i in range(3): #doctest: +ELLIPSIS
    ...     snooze(0.123) 
    snooze(0.123) dt=0...s
    snooze(0.123) dt=0...s
    snooze(0.123) dt=0...s
    """
