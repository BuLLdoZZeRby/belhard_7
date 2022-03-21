"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(number):
    if number > 0:
        fnum1, fnum2 = 0, 1
        for i in range(0, number):
            fnum1, fnum2 = fnum2, fnum1 + fnum2
            yield fnum1
    else:
        raise ValueError('Введите значение больше 1')
