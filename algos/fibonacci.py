from functools import cache
import time


def fib1(n: int):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


@cache
def fib2(n: int):
    if n <= 1:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


qty = 36
start_time = time.monotonic()
print(f'Fibonacci (uncached) of {qty} is {fib1(qty)}, done in {time.monotonic() - start_time}s')
start_time = time.monotonic()
print(f'Fibonacci (cached)   of {qty} is {fib2(qty)}, done in {time.monotonic() - start_time}s')
