"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    fnum1, fnum2 = 0, 1
    for i in range(0, 10):
        fnum1, fnum2 = fnum2, fnum1 + fnum2
        yield fnum1
