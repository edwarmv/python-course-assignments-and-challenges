# problem 1
print("problem 1")
from typing import Generator


def gensquares(n: int) -> Generator:
    for i in range(n):
        yield i**2


for x in gensquares(10):
    print(x)


# problem 2
print("problem 2")
import random


def rand_num(low: int, high: int, n: int) -> Generator:
    for _ in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


# problem 3
print("problem 3")
s = 'hello'
iter_s = iter(s)
print(next(iter_s))
