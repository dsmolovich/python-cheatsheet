import time

def clock(func):
    def clocked(*args):
        """
        >>> snooze(1)  #doctest: +ELLIPSIS
        [1...s] snooze(1) -> None
        
        >>> factorial(6)  #doctest: +ELLIPSIS
        [0...s] factorial(1) -> 1
        [0...s] factorial(2) -> 2
        [0...s] factorial(3) -> 6
        [0...s] factorial(4) -> 24
        [0...s] factorial(5) -> 120
        [0...s] factorial(6) -> 720
        720
        """
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

