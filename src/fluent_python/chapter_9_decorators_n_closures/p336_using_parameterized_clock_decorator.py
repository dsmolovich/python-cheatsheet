import time
from p334_parameterized_clock_decorator import clock

@clock('{name}({args}) dt={elapsed:0.3f}s')
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

if __name__ == '__main__':
    for i in range(3):
        snooze(0.123)