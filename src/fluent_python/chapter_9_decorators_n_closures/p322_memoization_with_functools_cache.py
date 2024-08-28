import functools
from p319_implementing_decorator import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@functools.cache
@clock
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n-2) + fibonacci_with_cache(n-1)


if __name__ == '__main__':
    num = 6
    print("===========================================")
    print(f"fibbonaci({num}):")
    print(fibonacci(num))
    print("===========================================")
    print(f"fibonacci_with_cache({num}):")
    print(fibonacci_with_cache(num))
