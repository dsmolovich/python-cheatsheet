def make_averager():
    """
    >>> avg = make_averager()
    >>> avg(10)
    10.0
    >>> avg(11)
    10.5
    >>> avg(12)
    11.0
    """
    count, total = 0, 0
    def averager (new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager